"""Persistence adapter for affiliate programs, referrals and attributed events.

No HTTP, provider SDK, or commission-policy decisions belong in this module.
"""
from __future__ import annotations

import json
import sqlite3
from typing import Any
from uuid import uuid4

from backend.database.service import DatabaseService
from .schema import EVENTS_TABLE, PROGRAMS_TABLE, REFERRALS_TABLE, schema_statements


class AffiliateMarketingRepository:
    """Owner-scoped repository backed by the central SUPREME database."""

    def __init__(self, database: DatabaseService | None = None, initialize: bool = True):
        self.database = database or DatabaseService()
        if initialize:
            self.initialize()

    def initialize(self) -> None:
        for statement in schema_statements():
            self.database.execute(statement)

    @staticmethod
    def _dict(row: sqlite3.Row | dict[str, Any] | None) -> dict[str, Any] | None:
        if row is None:
            return None
        item = dict(row)
        for field in ("metadata_json",):
            raw = item.pop(field, "{}")
            try:
                item["metadata"] = json.loads(raw)
            except (TypeError, ValueError):
                item["metadata"] = {}
        return item

    def upsert_program(
        self,
        *,
        program_id: str,
        platform_id: str,
        program_name: str,
        region: str = "GLOBAL",
        commission_type: str = "UNSPECIFIED",
        commission_rate: float = 0,
        currency: str = "USD",
        terms_url: str | None = None,
        verification_status: str = "UNVERIFIED",
        program_status: str = "PENDING_VERIFICATION",
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        self.database.execute(
            f"""INSERT INTO {PROGRAMS_TABLE}
            (program_id, platform_id, program_name, region, commission_type,
             commission_rate, currency, terms_url, verification_status,
             program_status, metadata_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(program_id) DO UPDATE SET
                platform_id=excluded.platform_id,
                program_name=excluded.program_name,
                region=excluded.region,
                commission_type=excluded.commission_type,
                commission_rate=excluded.commission_rate,
                currency=excluded.currency,
                terms_url=excluded.terms_url,
                verification_status=excluded.verification_status,
                program_status=excluded.program_status,
                metadata_json=excluded.metadata_json,
                updated_at=CURRENT_TIMESTAMP""",
            (
                program_id, platform_id, program_name, region, commission_type,
                float(commission_rate), currency, terms_url, verification_status,
                program_status, json.dumps(metadata or {}, sort_keys=True),
            ),
        )
        result = self.get_program(program_id)
        if result is None:
            raise RuntimeError("AFFILIATE_PROGRAM_WRITE_FAILED")
        return result

    def get_program(self, program_id: str) -> dict[str, Any] | None:
        row = self.database.fetchone(
            f"SELECT * FROM {PROGRAMS_TABLE} WHERE program_id = ?",
            (program_id,),
        )
        return self._dict(row)

    def list_programs(self, platform_id: str | None = None) -> list[dict[str, Any]]:
        if platform_id:
            rows = self.database.fetchall(
                f"SELECT * FROM {PROGRAMS_TABLE} WHERE platform_id = ? ORDER BY program_name",
                (platform_id,),
            )
        else:
            rows = self.database.fetchall(
                f"SELECT * FROM {PROGRAMS_TABLE} ORDER BY platform_id, program_name"
            )
        return [self._dict(row) or {} for row in rows]

    def create_referral(
        self,
        *,
        owner_user_id: str,
        program_id: str,
        referral_code: str,
        destination_url: str,
        disclosure_text: str,
    ) -> dict[str, Any]:
        referral_id = f"BB-AFF-{uuid4().hex}"
        self.database.execute(
            f"""INSERT INTO {REFERRALS_TABLE}
            (referral_id, owner_user_id, program_id, referral_code,
             destination_url, disclosure_text)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (referral_id, owner_user_id, program_id, referral_code,
             destination_url, disclosure_text),
        )
        return self.get_referral(referral_id) or {}

    def get_referral(self, referral_id: str) -> dict[str, Any] | None:
        row = self.database.fetchone(
            f"""SELECT r.*, p.platform_id, p.program_name, p.currency
            FROM {REFERRALS_TABLE} r
            JOIN {PROGRAMS_TABLE} p ON p.program_id = r.program_id
            WHERE r.referral_id = ?""",
            (referral_id,),
        )
        if row is None:
            return None
        return dict(row)

    def list_referrals(self, owner_user_id: str) -> list[dict[str, Any]]:
        rows = self.database.fetchall(
            f"""SELECT r.*, p.platform_id, p.program_name, p.currency
            FROM {REFERRALS_TABLE} r
            JOIN {PROGRAMS_TABLE} p ON p.program_id = r.program_id
            WHERE r.owner_user_id = ?
            ORDER BY r.created_at DESC""",
            (owner_user_id,),
        )
        return [dict(row) for row in rows]

    def record_event(
        self,
        *,
        referral_id: str,
        source_event_id: str,
        event_type: str,
        amount_minor: int,
        commission_minor: int,
        currency: str,
        event_status: str = "PENDING",
        occurred_at: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        event_id = f"BB-EVENT-{uuid4().hex}"
        self.database.execute(
            f"""INSERT INTO {EVENTS_TABLE}
            (event_id, referral_id, source_event_id, event_type, amount_minor,
             commission_minor, currency, event_status, occurred_at, metadata_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, COALESCE(?, CURRENT_TIMESTAMP), ?)
            ON CONFLICT(referral_id, source_event_id) DO NOTHING""",
            (
                event_id, referral_id, source_event_id, event_type,
                int(amount_minor), int(commission_minor), currency, event_status,
                occurred_at, json.dumps(metadata or {}, sort_keys=True),
            ),
        )
        row = self.database.fetchone(
            f"SELECT * FROM {EVENTS_TABLE} WHERE referral_id = ? AND source_event_id = ?",
            (referral_id, source_event_id),
        )
        if row is None:
            raise RuntimeError("AFFILIATE_EVENT_WRITE_FAILED")
        return self._dict(row) or {}

    def list_events(self, referral_id: str) -> list[dict[str, Any]]:
        rows = self.database.fetchall(
            f"SELECT * FROM {EVENTS_TABLE} WHERE referral_id = ? ORDER BY occurred_at DESC",
            (referral_id,),
        )
        return [self._dict(row) or {} for row in rows]


__all__ = ["AffiliateMarketingRepository"]
