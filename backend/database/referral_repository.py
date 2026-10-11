"""SQLite repository for GLOBAL CORE ECOSYSTEM people, referral links, events and commissions.

Uses the existing central DatabaseService and creates only namespaced tables.
It does not delete, replace, or migrate unrelated existing tables.
"""
from __future__ import annotations

import json
from typing import Any
from uuid import uuid4

from backend.database.service import DatabaseService


class ReferralRepository:
    TABLES = (
        "supreme_people",
        "supreme_referral_links",
        "supreme_referral_events",
        "supreme_commissions",
    )

    def __init__(self, database: DatabaseService | None = None) -> None:
        self.database = database or DatabaseService()
        self.initialize()

    def initialize(self) -> dict[str, object]:
        statements = (
            """CREATE TABLE IF NOT EXISTS supreme_people (
                person_id TEXT PRIMARY KEY,
                display_name TEXT NOT NULL,
                source_platform TEXT NOT NULL,
                need_category TEXT NOT NULL,
                situation_notes TEXT NOT NULL DEFAULT '',
                preferred_channel TEXT NOT NULL DEFAULT 'WHATSAPP',
                whatsapp_contact TEXT NOT NULL DEFAULT '',
                contact_consent INTEGER NOT NULL DEFAULT 0,
                response_stage TEXT NOT NULL DEFAULT 'NEW',
                next_follow_up_at TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS supreme_referral_links (
                referral_id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                program_name TEXT NOT NULL,
                referral_url TEXT NOT NULL,
                whatsapp_contact TEXT NOT NULL DEFAULT '',
                ownership_type TEXT NOT NULL DEFAULT 'PERSONAL',
                active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS supreme_referral_events (
                event_id TEXT PRIMARY KEY,
                person_id TEXT,
                referral_id TEXT,
                event_type TEXT NOT NULL,
                metadata_json TEXT NOT NULL DEFAULT '{}',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(person_id) REFERENCES supreme_people(person_id),
                FOREIGN KEY(referral_id) REFERENCES supreme_referral_links(referral_id)
            )""",
            """CREATE TABLE IF NOT EXISTS supreme_commissions (
                commission_id TEXT PRIMARY KEY,
                person_id TEXT,
                referral_id TEXT,
                partner_name TEXT NOT NULL,
                order_reference TEXT NOT NULL UNIQUE,
                amount_paise INTEGER NOT NULL CHECK(amount_paise >= 0),
                currency TEXT NOT NULL DEFAULT 'INR',
                status TEXT NOT NULL DEFAULT 'PENDING',
                evidence_reference TEXT NOT NULL DEFAULT '',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(person_id) REFERENCES supreme_people(person_id),
                FOREIGN KEY(referral_id) REFERENCES supreme_referral_links(referral_id)
            )""",
        )
        for statement in statements:
            self.database.execute(statement)
        return {"success": True, "tables": list(self.TABLES), "database": "CENTRAL_DATABASE_SERVICE"}

    @staticmethod
    def _dict(row: Any) -> dict[str, Any] | None:
        return dict(row) if row is not None else None

    def create_person(self, data: dict[str, Any]) -> dict[str, Any]:
        person_id = data.get("person_id") or f"PER-{uuid4().hex}"
        self.database.execute(
            """INSERT INTO supreme_people
            (person_id, display_name, source_platform, need_category, situation_notes,
             preferred_channel, whatsapp_contact, contact_consent, response_stage, next_follow_up_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                person_id, data["display_name"].strip(), data["source_platform"].strip(),
                data["need_category"].strip(), data.get("situation_notes", ""),
                data.get("preferred_channel", "WHATSAPP").upper(),
                data.get("whatsapp_contact", ""), int(bool(data.get("contact_consent", False))),
                data.get("response_stage", "NEW"), data.get("next_follow_up_at"),
            ),
        )
        self.record_event(person_id, None, "PERSON_CREATED", {"source_platform": data["source_platform"]})
        return self.get_person(person_id) or {}

    def get_person(self, person_id: str) -> dict[str, Any] | None:
        return self._dict(self.database.fetchone(
            "SELECT * FROM supreme_people WHERE person_id = ?", (person_id,)
        ))

    def list_people(self, response_stage: str | None = None, limit: int = 100) -> list[dict[str, Any]]:
        safe_limit = max(1, min(int(limit), 500))
        if response_stage:
            rows = self.database.fetchall(
                "SELECT * FROM supreme_people WHERE response_stage = ? ORDER BY created_at DESC LIMIT ?",
                (response_stage, safe_limit),
            )
        else:
            rows = self.database.fetchall(
                "SELECT * FROM supreme_people ORDER BY created_at DESC LIMIT ?", (safe_limit,)
            )
        return [dict(row) for row in rows]

    def update_person_stage(self, person_id: str, stage: str, next_follow_up_at: str | None = None) -> dict[str, Any] | None:
        existing = self.get_person(person_id)
        if not existing:
            return None
        self.database.execute(
            """UPDATE supreme_people SET response_stage = ?, next_follow_up_at = ?,
            contact_consent = CASE WHEN ? = 'DO_NOT_CONTACT' THEN 0 ELSE contact_consent END,
            updated_at = CURRENT_TIMESTAMP WHERE person_id = ?""",
            (stage, next_follow_up_at, stage, person_id),
        )
        self.record_event(person_id, None, "PERSON_STAGE_CHANGED", {"from": existing["response_stage"], "to": stage, "next_follow_up_at": next_follow_up_at})
        return self.get_person(person_id)

    def create_referral_link(self, data: dict[str, Any]) -> dict[str, Any]:
        referral_id = data.get("referral_id") or f"REF-{uuid4().hex}"
        self.database.execute(
            """INSERT INTO supreme_referral_links
            (referral_id, platform, program_name, referral_url, whatsapp_contact, ownership_type, active)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                referral_id, data["platform"].strip().upper(), data["program_name"].strip(),
                data["referral_url"].strip(), data.get("whatsapp_contact", ""),
                data.get("ownership_type", "PERSONAL").strip().upper(), int(bool(data.get("active", True))),
            ),
        )
        return self.get_referral_link(referral_id) or {}

    def get_referral_link(self, referral_id: str) -> dict[str, Any] | None:
        return self._dict(self.database.fetchone(
            "SELECT * FROM supreme_referral_links WHERE referral_id = ?", (referral_id,)
        ))

    def list_referral_links(self, platform: str | None = None, active_only: bool = False) -> list[dict[str, Any]]:
        query = "SELECT * FROM supreme_referral_links WHERE 1=1"
        params: list[Any] = []
        if platform:
            query += " AND platform = ?"
            params.append(platform.strip().upper())
        if active_only:
            query += " AND active = 1"
        query += " ORDER BY created_at DESC"
        return [dict(row) for row in self.database.fetchall(query, params)]

    def record_event(self, person_id: str | None, referral_id: str | None, event_type: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        event_id = f"EVT-{uuid4().hex}"
        payload = json.dumps(metadata or {}, ensure_ascii=False, sort_keys=True)
        self.database.execute(
            """INSERT INTO supreme_referral_events
            (event_id, person_id, referral_id, event_type, metadata_json)
            VALUES (?, ?, ?, ?, ?)""",
            (event_id, person_id, referral_id, event_type.strip().upper(), payload),
        )
        return {"event_id": event_id, "person_id": person_id, "referral_id": referral_id, "event_type": event_type.upper(), "metadata": metadata or {}}

    def list_events(self, person_id: str | None = None, limit: int = 100) -> list[dict[str, Any]]:
        safe_limit = max(1, min(int(limit), 500))
        if person_id:
            rows = self.database.fetchall(
                "SELECT * FROM supreme_referral_events WHERE person_id = ? ORDER BY created_at DESC LIMIT ?",
                (person_id, safe_limit),
            )
        else:
            rows = self.database.fetchall(
                "SELECT * FROM supreme_referral_events ORDER BY created_at DESC LIMIT ?", (safe_limit,)
            )
        results = []
        for row in rows:
            item = dict(row)
            item["metadata"] = json.loads(item.pop("metadata_json") or "{}")
            results.append(item)
        return results

    def create_commission(self, data: dict[str, Any]) -> dict[str, Any]:
        commission_id = data.get("commission_id") or f"COM-{uuid4().hex}"
        self.database.execute(
            """INSERT INTO supreme_commissions
            (commission_id, person_id, referral_id, partner_name, order_reference,
             amount_paise, currency, status, evidence_reference)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'PENDING', ?)""",
            (
                commission_id, data.get("person_id"), data.get("referral_id"),
                data["partner_name"].strip(), data["order_reference"].strip(),
                int(data["amount_paise"]), data.get("currency", "INR").upper(),
                data.get("evidence_reference", ""),
            ),
        )
        self.record_event(data.get("person_id"), data.get("referral_id"), "COMMISSION_RECORDED", {"commission_id": commission_id, "order_reference": data["order_reference"], "amount_paise": int(data["amount_paise"]), "status": "PENDING"})
        return self.get_commission(commission_id) or {}

    def get_commission(self, commission_id: str) -> dict[str, Any] | None:
        return self._dict(self.database.fetchone(
            "SELECT * FROM supreme_commissions WHERE commission_id = ?", (commission_id,)
        ))

    def update_commission_status(self, commission_id: str, status: str) -> dict[str, Any] | None:
        existing = self.get_commission(commission_id)
        if not existing:
            return None
        self.database.execute(
            "UPDATE supreme_commissions SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE commission_id = ?",
            (status, commission_id),
        )
        self.record_event(existing.get("person_id"), existing.get("referral_id"), "COMMISSION_STATUS_CHANGED", {"commission_id": commission_id, "from": existing["status"], "to": status})
        return self.get_commission(commission_id)

    def list_commissions(self, status: str | None = None, limit: int = 100) -> list[dict[str, Any]]:
        safe_limit = max(1, min(int(limit), 500))
        if status:
            rows = self.database.fetchall(
                "SELECT * FROM supreme_commissions WHERE status = ? ORDER BY created_at DESC LIMIT ?",
                (status.upper(), safe_limit),
            )
        else:
            rows = self.database.fetchall(
                "SELECT * FROM supreme_commissions ORDER BY created_at DESC LIMIT ?", (safe_limit,)
            )
        return [dict(row) for row in rows]
