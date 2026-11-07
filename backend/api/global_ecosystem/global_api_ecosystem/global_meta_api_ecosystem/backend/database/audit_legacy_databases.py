"""Audit and optionally migrate legacy SQLite files into the SUPREME database.

Default mode is read-only. Use --apply only after reviewing the audit output.
The migrator never deletes source files or overwrites conflicting target rows.
"""
from __future__ import annotations

import argparse
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_TARGET = Path(os.getenv("SUPREME_DB_PATH") or "data/supreme.db")
DEFAULT_SOURCES = (
    Path("main_base_foundation.db"),
    Path("data/main_base_foundation.db"),
    Path("supreme.db"),
    Path("supremesetuhub.db"),
    Path("supreme_identities.db"),
    Path("data/supreme_identities.db"),
    Path("app/supreme_identities.db"),
    Path("supreme_personal_ai.db"),
    Path("data/supreme_personal_ai.db"),
)


def _tables(connection: sqlite3.Connection) -> list[str]:
    rows = connection.execute(
        "SELECT name FROM sqlite_master "
        "WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ).fetchall()
    return [str(row[0]) for row in rows]


def _columns(connection: sqlite3.Connection, table: str) -> list[str]:
    # Table names originate from sqlite_master, not from user input.
    return [str(row[1]) for row in connection.execute(
        f'PRAGMA table_info("{table.replace(chr(34), chr(34) * 2)}")'
    ).fetchall()]


def _schema(connection: sqlite3.Connection, table: str) -> str | None:
    row = connection.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name=?",
        (table,),
    ).fetchone()
    return str(row[0]) if row and row[0] else None


def audit(target_path: Path, sources: tuple[Path, ...]) -> dict[str, Any]:
    report: dict[str, Any] = {"target": str(target_path), "sources": []}
    if target_path.exists():
        with sqlite3.connect(str(target_path)) as target:
            report["target_tables"] = {
                table: target.execute(
                    f'SELECT COUNT(*) FROM "{table.replace(chr(34), chr(34) * 2)}"'
                ).fetchone()[0]
                for table in _tables(target)
            }
    else:
        report["target_tables"] = {}

    for source_path in sources:
        if not source_path.exists() or source_path.resolve() == target_path.resolve():
            continue
        entry: dict[str, Any] = {"path": str(source_path), "tables": {}}
        try:
            with sqlite3.connect(str(source_path)) as source:
                for table in _tables(source):
                    entry["tables"][table] = {
                        "rows": source.execute(
                            f'SELECT COUNT(*) FROM "{table.replace(chr(34), chr(34) * 2)}"'
                        ).fetchone()[0],
                        "columns": _columns(source, table),
                        "already_in_target": table in report["target_tables"],
                    }
        except sqlite3.DatabaseError as exc:
            entry["error"] = str(exc)
        report["sources"].append(entry)
    return report


def migrate(target_path: Path, sources: tuple[Path, ...]) -> dict[str, Any]:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    if target_path.exists():
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup_path = target_path.with_name(f"{target_path.name}.{stamp}.bak")
        with sqlite3.connect(str(target_path)) as live, sqlite3.connect(str(backup_path)) as backup:
            live.backup(backup)
    else:
        backup_path = None

    results: list[dict[str, Any]] = []
    with sqlite3.connect(str(target_path)) as target:
        target.execute("PRAGMA foreign_keys = ON")
        for source_path in sources:
            if not source_path.exists() or source_path.resolve() == target_path.resolve():
                continue
            source_result: dict[str, Any] = {"path": str(source_path), "tables": []}
            try:
                with sqlite3.connect(str(source_path)) as source:
                    source.row_factory = sqlite3.Row
                    for table in _tables(source):
                        escaped = table.replace('"', '""')
                        source_columns = _columns(source, table)
                        target_tables = _tables(target)
                        if table not in target_tables:
                            create_sql = _schema(source, table)
                            if not create_sql:
                                source_result["tables"].append({
                                    "table": table, "status": "SKIPPED_NO_SCHEMA"
                                })
                                continue
                            target.execute(create_sql)
                            target.commit()
                            target_tables = _tables(target)

                        target_columns = _columns(target, table)
                        if source_columns != target_columns:
                            source_result["tables"].append({
                                "table": table,
                                "status": "SKIPPED_SCHEMA_MISMATCH",
                                "source_columns": source_columns,
                                "target_columns": target_columns,
                            })
                            continue

                        before = target.total_changes
                        placeholders = ", ".join("?" for _ in source_columns)
                        column_sql = ", ".join(
                            '"' + column.replace('"', '""') + '"'
                            for column in source_columns
                        )
                        rows = source.execute(
                            f'SELECT * FROM "{escaped}"'
                        ).fetchall()
                        for row in rows:
                            target.execute(
                                f'INSERT OR IGNORE INTO "{escaped}" ({column_sql}) '
                                f'VALUES ({placeholders})',
                                tuple(row[column] for column in source_columns),
                            )
                        target.commit()
                        inserted = target.total_changes - before
                        source_result["tables"].append({
                            "table": table,
                            "status": "COPIED_WITH_CONFLICT_CHECK",
                            "source_rows": len(rows),
                            "inserted_rows": inserted,
                            "skipped_or_conflicting_rows": len(rows) - inserted,
                        })
            except sqlite3.DatabaseError as exc:
                source_result["error"] = str(exc)
            results.append(source_result)
    return {"target": str(target_path), "backup": str(backup_path) if backup_path else None, "results": results}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--sources", type=Path, nargs="*", default=list(DEFAULT_SOURCES))
    parser.add_argument("--apply", action="store_true", help="Apply safe copy after backup; default is read-only audit.")
    args = parser.parse_args()
    result = migrate(args.target, tuple(args.sources)) if args.apply else audit(args.target, tuple(args.sources))
    import json
    print(json.dumps(result, indent=2, default=str))
    if not args.apply:
        print("\nREAD-ONLY AUDIT ONLY. Re-run with --apply after reviewing schema conflicts.")


if __name__ == "__main__":
    main()
