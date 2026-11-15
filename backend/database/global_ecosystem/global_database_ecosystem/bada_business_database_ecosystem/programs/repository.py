"""Owner-scoped SQLite repository for Bada Business program snapshots."""

from __future__ import annotations

import json
from uuid import uuid4
from typing import Any

from backend.database.service import DatabaseService
from .models import BadaBusinessProgramRecord
from .schema import schema_statements, PROGRAM_TABLE, SCHEMA_VERSION


class BadaBusinessProgramRepository:
    def __init__(self, database: DatabaseService | None = None):
        self.database = database or DatabaseService()
        self.initialize()

    def initialize(self):
        for statement in schema_statements():
            self.database.execute(statement)
        self.database.execute(
            "INSERT OR IGNORE INTO bada_business_program_migrations (migration_id) VALUES (?)",
            (SCHEMA_VERSION,),
        )

    @staticmethod
    def _deserialize(row: Any):
        item = dict(row)
        try:
            item["snapshot"] = json.loads(item.pop("snapshot_json", "{}"))
        except (TypeError, ValueError):
            item["snapshot"] = {}
        return item

    def upsert(self, record: BadaBusinessProgramRecord):
        record.validate()
        existing = self.get(record.owner_user_id, record.program_id)
        record_id = existing["record_id"] if existing else f"BB-PROGRAM-{uuid4().hex}"
        self.database.execute(
            f"""INSERT INTO {PROGRAM_TABLE}
            (record_id, owner_user_id, program_id, provider_id, program_name,
             program_status, source_catalog, source_version, snapshot_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(owner_user_id, program_id) DO UPDATE SET
                provider_id = excluded.provider_id,
                program_name = excluded.program_name,
                program_status = excluded.program_status,
                source_catalog = excluded.source_catalog,
                source_version = excluded.source_version,
                snapshot_json = excluded.snapshot_json,
                updated_at = CURRENT_TIMESTAMP""",
            (
                record_id, record.owner_user_id, record.program_id,
                record.provider_id, record.program_name, record.program_status,
                record.source_catalog, record.source_version,
                json.dumps(record.snapshot, ensure_ascii=False, sort_keys=True),
            ),
        )
        return self.get(record.owner_user_id, record.program_id)

    def get(self, owner_user_id: str, program_id: str):
        row = self.database.fetchone(
            f"SELECT * FROM {PROGRAM_TABLE} WHERE owner_user_id = ? AND program_id = ?",
            (owner_user_id, program_id),
        )
        return self._deserialize(row) if row is not None else None

    def list(self, owner_user_id: str, *, program_status: str | None = None, limit: int = 100):
        if not isinstance(limit, int) or limit < 1 or limit > 500:
            raise ValueError("limit must be between 1 and 500")
        if program_status:
            rows = self.database.fetchall(
                f"""SELECT * FROM {PROGRAM_TABLE}
                WHERE owner_user_id = ? AND program_status = ?
                ORDER BY updated_at DESC, program_name LIMIT ?""",
                (owner_user_id, program_status, limit),
            )
        else:
            rows = self.database.fetchall(
                f"""SELECT * FROM {PROGRAM_TABLE}
                WHERE owner_user_id = ?
                ORDER BY updated_at DESC, program_name LIMIT ?""",
                (owner_user_id, limit),
            )
        return [self._deserialize(row) for row in rows]

    def delete(self, owner_user_id: str, program_id: str):
        cursor = self.database.execute(
            f"DELETE FROM {PROGRAM_TABLE} WHERE owner_user_id = ? AND program_id = ?",
            (owner_user_id, program_id),
        )
        return cursor.rowcount > 0
