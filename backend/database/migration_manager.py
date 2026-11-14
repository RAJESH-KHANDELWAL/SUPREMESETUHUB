"""Checksum-tracked SQL migration runner for the central SUPREME database.

Migrations are applied in lexical order from backend/database/migrations/mysql.
A backup should be taken before every production migration. MySQL DDL is not
fully transactional, so this runner never claims rollback support.
"""
from __future__ import annotations

import hashlib
import os
import re
from pathlib import Path
from typing import Any

import pymysql

from backend.database.gde_connection import SupremeDatabaseConfig


class DatabaseMigrationManager:
    def __init__(
        self,
        config: SupremeDatabaseConfig | None = None,
        migrations_dir: str | Path | None = None,
    ) -> None:
        self.config = config or SupremeDatabaseConfig.from_environment()
        self.migrations_dir = Path(
            migrations_dir or Path(__file__).parent / "migrations" / "mysql"
        ).resolve()

    @staticmethod
    def _statements(sql: str) -> list[str]:
        # Project migrations must not contain stored procedures or semicolons
        # inside quoted strings. Keep each DDL/DML statement on normal SQL syntax.
        cleaned = "\n".join(
            line for line in sql.splitlines()
            if not line.lstrip().startswith("--")
        )
        return [part.strip() for part in cleaned.split(";") if part.strip()]

    def _connect(self):
        self.config.validate()
        options: dict[str, Any] = {
            "host": self.config.host,
            "user": self.config.username,
            "password": self.config.password,
            "database": self.config.database,
            "port": self.config.port,
            "connect_timeout": self.config.connect_timeout,
            "charset": "utf8mb4",
            "cursorclass": pymysql.cursors.DictCursor,
            "autocommit": False,
        }
        if self.config.ssl_ca:
            options.update(ssl_ca=self.config.ssl_ca, ssl_verify_cert=True, ssl_verify_identity=True)
        return pymysql.connect(**options)

    def status(self) -> dict[str, object]:
        if not self.migrations_dir.is_dir():
            raise FileNotFoundError("MySQL migrations directory does not exist.")
        files = sorted(self.migrations_dir.glob("*.sql"))
        return {
            "database": self.config.database,
            "migration_directory": str(self.migrations_dir),
            "available": [
                {"name": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                for path in files
            ],
        }

    def apply_pending(self, *, dry_run: bool = True) -> dict[str, object]:
        self.config.validate()
        if not self.migrations_dir.is_dir():
            raise FileNotFoundError("MySQL migrations directory does not exist.")
        files = sorted(self.migrations_dir.glob("*.sql"))
        for path in files:
            if not re.fullmatch(r"[0-9]{3}_[a-z0-9_]+\.sql", path.name):
                raise ValueError(f"Migration filename is not versioned safely: {path.name}")
        if dry_run:
            return {
                "success": True,
                "dry_run": True,
                "database": self.config.database,
                "pending": [path.name for path in files],
                "applied": [],
                "warning": "No SQL was executed. Take a verified backup before production apply.",
            }

        connection = self._connect()
        applied: list[str] = []
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS ss_schema_migrations (
                        migration_name VARCHAR(190) NOT NULL PRIMARY KEY,
                        checksum_sha256 CHAR(64) NOT NULL,
                        applied_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""
                )
                for path in files:
                    sql = path.read_text(encoding="utf-8")
                    checksum = hashlib.sha256(sql.encode("utf-8")).hexdigest()
                    cursor.execute(
                        "SELECT checksum_sha256 FROM ss_schema_migrations WHERE migration_name=%s",
                        (path.name,),
                    )
                    existing = cursor.fetchone()
                    if existing:
                        if existing["checksum_sha256"] != checksum:
                            raise RuntimeError(f"Applied migration checksum changed: {path.name}")
                        continue
                    for statement in self._statements(sql):
                        cursor.execute(statement)
                    cursor.execute(
                        "INSERT INTO ss_schema_migrations (migration_name, checksum_sha256) VALUES (%s, %s)",
                        (path.name, checksum),
                    )
                    connection.commit()
                    applied.append(path.name)
            return {
                "success": True,
                "dry_run": False,
                "database": self.config.database,
                "applied": applied,
                "warning": "MySQL DDL may auto-commit; recover from the verified pre-migration backup if needed.",
            }
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()
