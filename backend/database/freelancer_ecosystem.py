"""Central-database persistence for GLOBAL FREELANCER ECOSYSTEM.

Only metadata and JSON payloads live here. File bytes remain in the central
storage engine; this repository stores references to authorized storage assets.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from backend.database.service import DatabaseService


RECORD_TYPES = {
    "PROFILE",
    "SERVICE",
    "PORTFOLIO",
    "PROJECT",
    "APPLICATION",
    "WORK_HISTORY",
}
RECORD_STATUSES = {"DRAFT", "ACTIVE", "ARCHIVED"}


class FreelancerEcosystemRepository:
    """Store owner-scoped freelancer records in the shared central database."""

    def __init__(self, db_path: str | None = None) -> None:
        self.database = DatabaseService(db_path=db_path)
        self.initialize()

    @staticmethod
    def _now() -> str:
        return datetime.now(timezone.utc).isoformat()

    def initialize(self) -> None:
        # Additive table only; does not alter or delete existing application data.
        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS freelancer_ecosystem_records (
                record_id TEXT PRIMARY KEY,
                owner_id TEXT NOT NULL,
                record_type TEXT NOT NULL,
                title TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'DRAFT',
                payload_json TEXT NOT NULL DEFAULT '{}',
                storage_asset_ids_json TEXT NOT NULL DEFAULT '[]',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )
        self.database.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_freelancer_records_owner_type
            ON freelancer_ecosystem_records(owner_id, record_type, updated_at)
            """
        )

    @staticmethod
    def _decode(row: Any) -> dict[str, Any]:
        result = dict(row)
        result["payload"] = json.loads(result.pop("payload_json") or "{}")
        result["storage_asset_ids"] = json.loads(
            result.pop("storage_asset_ids_json") or "[]"
        )
        return result

    def create(
        self,
        *,
        owner_id: str,
        record_type: str,
        title: str,
        payload: dict[str, Any],
        storage_asset_ids: list[str] | None = None,
        status: str = "DRAFT",
    ) -> dict[str, Any]:
        owner = str(owner_id or "").strip()
        kind = str(record_type or "").strip().upper()
        label = str(title or "").strip()
        state = str(status or "DRAFT").strip().upper()
        if not owner:
            raise ValueError("AUTHENTICATED_OWNER_REQUIRED")
        if kind not in RECORD_TYPES:
            raise ValueError("UNSUPPORTED_FREELANCER_RECORD_TYPE")
        if not label or len(label) > 180:
            raise ValueError("TITLE_MUST_BE_1_TO_180_CHARACTERS")
        if state not in RECORD_STATUSES:
            raise ValueError("UNSUPPORTED_RECORD_STATUS")
        if not isinstance(payload, dict):
            raise ValueError("PAYLOAD_MUST_BE_AN_OBJECT")
        if len(json.dumps(payload, ensure_ascii=False, default=str)) > 100_000:
            raise ValueError("PAYLOAD_TOO_LARGE")
        asset_ids = [str(item).strip() for item in (storage_asset_ids or [])]
        if len(asset_ids) > 50 or any(not item or len(item) > 160 for item in asset_ids):
            raise ValueError("INVALID_STORAGE_ASSET_REFERENCES")

        now = self._now()
        record_id = f"FRE-{uuid4().hex.upper()}"
        self.database.execute(
            """
            INSERT INTO freelancer_ecosystem_records (
                record_id, owner_id, record_type, title, status,
                payload_json, storage_asset_ids_json, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record_id, owner, kind, label, state,
                json.dumps(payload, ensure_ascii=False, default=str),
                json.dumps(asset_ids),
                now, now,
            ),
        )
        return self.get(record_id, owner_id=owner)  # type: ignore[return-value]

    def list_for_owner(
        self,
        *,
        owner_id: str,
        record_type: str | None = None,
        limit: int = 50,
    ) -> list[dict[str, Any]]:
        owner = str(owner_id or "").strip()
        if not owner:
            raise ValueError("AUTHENTICATED_OWNER_REQUIRED")
        bounded_limit = max(1, min(int(limit), 100))
        if record_type:
            kind = record_type.strip().upper()
            if kind not in RECORD_TYPES:
                raise ValueError("UNSUPPORTED_FREELANCER_RECORD_TYPE")
            rows = self.database.fetchall(
                """SELECT * FROM freelancer_ecosystem_records
                   WHERE owner_id = ? AND record_type = ?
                   ORDER BY updated_at DESC LIMIT ?""",
                (owner, kind, bounded_limit),
            )
        else:
            rows = self.database.fetchall(
                """SELECT * FROM freelancer_ecosystem_records
                   WHERE owner_id = ?
                   ORDER BY updated_at DESC LIMIT ?""",
                (owner, bounded_limit),
            )
        return [self._decode(row) for row in rows]

    def get(self, record_id: str, *, owner_id: str) -> dict[str, Any] | None:
        row = self.database.fetchone(
            """SELECT * FROM freelancer_ecosystem_records
               WHERE record_id = ? AND owner_id = ? LIMIT 1""",
            (str(record_id or "").strip(), str(owner_id or "").strip()),
        )
        return self._decode(row) if row else None
