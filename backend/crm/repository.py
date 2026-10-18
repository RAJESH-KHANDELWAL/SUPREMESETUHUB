"""Persistent, user-scoped storage for the shared CRM module."""
from __future__ import annotations

import json
from typing import Any
from uuid import uuid4

from backend.database.service import DatabaseService


class CRMRepository:
    """Owns CRM tables in the central database; never reads private-CRM tables."""

    CONTACT_COLUMNS = {
        "whatsapp_phone": "TEXT NOT NULL DEFAULT ''",
        "address": "TEXT NOT NULL DEFAULT ''",
        "city": "TEXT NOT NULL DEFAULT ''",
        "pincode": "TEXT NOT NULL DEFAULT ''",
        "designation": "TEXT NOT NULL DEFAULT ''",
        "verification_status": "TEXT NOT NULL DEFAULT 'UNVERIFIED'",
        "verification_evidence": "TEXT NOT NULL DEFAULT ''",
        "verified_at": "TEXT",
    }

    def __init__(self, database: DatabaseService | None = None) -> None:
        self.database = database or DatabaseService()
        self.initialize()

    def initialize(self) -> None:
        statements = (
            """CREATE TABLE IF NOT EXISTS crm_contacts (
                contact_id TEXT PRIMARY KEY,
                owner_user_id TEXT NOT NULL,
                full_name TEXT NOT NULL,
                email TEXT NOT NULL DEFAULT '',
                phone TEXT NOT NULL DEFAULT '',
                whatsapp_phone TEXT NOT NULL DEFAULT '',
                organization TEXT NOT NULL DEFAULT '',
                address TEXT NOT NULL DEFAULT '',
                city TEXT NOT NULL DEFAULT '',
                pincode TEXT NOT NULL DEFAULT '',
                designation TEXT NOT NULL DEFAULT '',
                verification_status TEXT NOT NULL DEFAULT 'UNVERIFIED',
                verification_evidence TEXT NOT NULL DEFAULT '',
                verified_at TEXT,
                source TEXT NOT NULL DEFAULT 'MANUAL',
                external_id TEXT NOT NULL DEFAULT '',
                notes TEXT NOT NULL DEFAULT '',
                tags_json TEXT NOT NULL DEFAULT '[]',
                consent_to_contact INTEGER NOT NULL DEFAULT 0,
                contact_status TEXT NOT NULL DEFAULT 'ACTIVE',
                category TEXT NOT NULL DEFAULT 'UNCATEGORIZED',
                follow_up_at TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )""",
            "CREATE INDEX IF NOT EXISTS idx_crm_contacts_owner_updated ON crm_contacts(owner_user_id, updated_at DESC)",
            "CREATE INDEX IF NOT EXISTS idx_crm_contacts_owner_email ON crm_contacts(owner_user_id, email)",
            """CREATE TABLE IF NOT EXISTS crm_audit_log (
                event_id TEXT PRIMARY KEY,
                owner_user_id TEXT NOT NULL,
                contact_id TEXT,
                actor_user_id TEXT NOT NULL,
                action TEXT NOT NULL,
                details_json TEXT NOT NULL DEFAULT '{}',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )""",
            "CREATE INDEX IF NOT EXISTS idx_crm_audit_owner_created ON crm_audit_log(owner_user_id, created_at DESC)",
            """CREATE TABLE IF NOT EXISTS crm_daily_items (
                item_id TEXT PRIMARY KEY,
                owner_user_id TEXT NOT NULL,
                actor_user_id TEXT NOT NULL,
                contact_id TEXT,
                item_type TEXT NOT NULL DEFAULT 'TASK',
                title TEXT NOT NULL,
                details TEXT NOT NULL DEFAULT '',
                due_at TEXT,
                status TEXT NOT NULL DEFAULT 'OPEN',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )""",
            "CREATE INDEX IF NOT EXISTS idx_crm_daily_items_owner_due ON crm_daily_items(owner_user_id, status, due_at)",
            """CREATE TABLE IF NOT EXISTS crm_contact_activities (
                activity_id TEXT PRIMARY KEY,
                owner_user_id TEXT NOT NULL,
                actor_user_id TEXT NOT NULL,
                contact_id TEXT NOT NULL,
                activity_type TEXT NOT NULL,
                summary TEXT NOT NULL,
                details TEXT NOT NULL DEFAULT '',
                outcome TEXT NOT NULL DEFAULT '',
                next_follow_up_at TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )""",
            "CREATE INDEX IF NOT EXISTS idx_crm_activities_owner_contact_time ON crm_contact_activities(owner_user_id, contact_id, created_at DESC)",
        )
        for statement in statements:
            self.database.execute(statement)

        # Safe additive migration for existing CRM databases.
        existing = {str(row["name"]) for row in self.database.fetchall("PRAGMA table_info(crm_contacts)")}
        for column, definition in self.CONTACT_COLUMNS.items():
            if column not in existing:
                self.database.execute(f"ALTER TABLE crm_contacts ADD COLUMN {column} {definition}")

    @staticmethod
    def _contact(row: Any) -> dict[str, Any]:
        item = dict(row)
        try:
            item["tags"] = json.loads(item.pop("tags_json", "[]"))
        except (TypeError, ValueError):
            item["tags"] = []
        item["consent_to_contact"] = bool(item.get("consent_to_contact"))
        return item

    def create_contact(self, owner_user_id: str, data: dict[str, Any]) -> dict[str, Any]:
        contact_id = data.get("contact_id")
        if not contact_id or contact_id == "pending":
            contact_id = f"CRM-{uuid4().hex}"
        self.database.execute(
            """INSERT INTO crm_contacts
            (contact_id, owner_user_id, full_name, email, phone, whatsapp_phone,
             organization, address, city, pincode, designation, verification_status,
             verification_evidence, verified_at, source, external_id, notes, tags_json,
             consent_to_contact, contact_status, category, follow_up_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                contact_id, owner_user_id, data["full_name"], data.get("email", ""),
                data.get("phone", ""), data.get("whatsapp_phone", ""),
                data.get("organization", ""), data.get("address", ""),
                data.get("city", ""), data.get("pincode", ""),
                data.get("designation", ""), data.get("verification_status", "UNVERIFIED"),
                data.get("verification_evidence", ""), data.get("verified_at"), data.get("source", "MANUAL"), data.get("external_id", ""),
                data.get("notes", ""), json.dumps(data.get("tags", [])),
                int(bool(data.get("consent_to_contact", False))),
                data.get("contact_status", "ACTIVE"),
                data.get("category", "UNCATEGORIZED"), data.get("follow_up_at"),
            ),
        )
        return self.get_contact(owner_user_id, contact_id)  # type: ignore[return-value]

    def get_contact(self, owner_user_id: str, contact_id: str) -> dict[str, Any] | None:
        row = self.database.fetchone(
            "SELECT * FROM crm_contacts WHERE owner_user_id = ? AND contact_id = ?",
            (owner_user_id, contact_id),
        )
        return self._contact(row) if row is not None else None

    def list_contacts(
        self, owner_user_id: str, *, category: str | None = None,
        contact_status: str | None = None, limit: int = 100,
    ) -> list[dict[str, Any]]:
        clauses = ["owner_user_id = ?"]
        params: list[Any] = [owner_user_id]
        if category:
            clauses.append("category = ?")
            params.append(category)
        if contact_status:
            clauses.append("contact_status = ?")
            params.append(contact_status)
        params.append(limit)
        rows = self.database.fetchall(
            f"SELECT * FROM crm_contacts WHERE {' AND '.join(clauses)} ORDER BY updated_at DESC, full_name LIMIT ?",
            params,
        )
        return [self._contact(row) for row in rows]

    def update_contact(self, owner_user_id: str, contact_id: str, changes: dict[str, Any]) -> dict[str, Any] | None:
        columns = {
            "full_name": "full_name", "email": "email", "phone": "phone",
            "whatsapp_phone": "whatsapp_phone", "organization": "organization",
            "address": "address", "city": "city", "pincode": "pincode",
            "designation": "designation", "verification_status": "verification_status",
            "verification_evidence": "verification_evidence", "verified_at": "verified_at",
            "source": "source", "external_id": "external_id", "notes": "notes",
            "tags": "tags_json", "consent_to_contact": "consent_to_contact",
            "contact_status": "contact_status", "category": "category", "follow_up_at": "follow_up_at",
        }
        updates = [(columns[key], value) for key, value in changes.items() if key in columns]
        if not updates:
            return self.get_contact(owner_user_id, contact_id)
        assignments = []
        params: list[Any] = []
        for column, value in updates:
            assignments.append(f"{column} = ?")
            if column == "tags_json":
                value = json.dumps(value)
            elif column == "consent_to_contact":
                value = int(bool(value))
            params.append(value)
        assignments.append("updated_at = CURRENT_TIMESTAMP")
        params.extend([owner_user_id, contact_id])
        self.database.execute(
            f"UPDATE crm_contacts SET {', '.join(assignments)} WHERE owner_user_id = ? AND contact_id = ?",
            params,
        )
        return self.get_contact(owner_user_id, contact_id)

    def delete_contact(self, owner_user_id: str, contact_id: str) -> bool:
        cursor = self.database.execute(
            "DELETE FROM crm_contacts WHERE owner_user_id = ? AND contact_id = ?",
            (owner_user_id, contact_id),
        )
        return cursor.rowcount > 0

    def log_event(self, owner_user_id: str, actor_user_id: str, action: str,
                  contact_id: str | None = None, details: dict[str, Any] | None = None) -> None:
        self.database.execute(
            """INSERT INTO crm_audit_log
            (event_id, owner_user_id, contact_id, actor_user_id, action, details_json)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (f"CRM-AUDIT-{uuid4().hex}", owner_user_id, contact_id,
             actor_user_id, action, json.dumps(details or {}, sort_keys=True)),
        )

    def list_audit_events(self, owner_user_id: str, limit: int = 100) -> list[dict[str, Any]]:
        rows = self.database.fetchall(
            """SELECT event_id, owner_user_id, contact_id, actor_user_id, action,
                      details_json, created_at
               FROM crm_audit_log WHERE owner_user_id = ?
               ORDER BY created_at DESC LIMIT ?""", (owner_user_id, limit),
        )
        events = []
        for row in rows:
            item = dict(row)
            try:
                item["details"] = json.loads(item.pop("details_json", "{}"))
            except (TypeError, ValueError):
                item["details"] = {}
            events.append(item)
        return events


    def create_activity(self, owner_user_id: str, actor_user_id: str, data: dict[str, Any]) -> dict[str, Any]:
        activity_id = f"CRM-ACT-{uuid4().hex}"
        self.database.execute(
            """INSERT INTO crm_contact_activities
            (activity_id, owner_user_id, actor_user_id, contact_id, activity_type,
             summary, details, outcome, next_follow_up_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (activity_id, owner_user_id, actor_user_id, data["contact_id"],
             data.get("activity_type", "NOTE"), data["summary"], data.get("details", ""),
             data.get("outcome", ""), data.get("next_follow_up_at")),
        )
        self.log_event(owner_user_id, actor_user_id, "CONTACT_ACTIVITY_LOGGED", data["contact_id"],
                       {"activity_id": activity_id, "activity_type": data.get("activity_type", "NOTE")})
        return self.get_activity(owner_user_id, activity_id)  # type: ignore[return-value]

    def get_activity(self, owner_user_id: str, activity_id: str) -> dict[str, Any] | None:
        row = self.database.fetchone(
            "SELECT * FROM crm_contact_activities WHERE owner_user_id = ? AND activity_id = ?",
            (owner_user_id, activity_id),
        )
        return dict(row) if row is not None else None

    def list_activities(self, owner_user_id: str, contact_id: str, limit: int = 100) -> list[dict[str, Any]]:
        rows = self.database.fetchall(
            """SELECT * FROM crm_contact_activities
               WHERE owner_user_id = ? AND contact_id = ?
               ORDER BY created_at DESC LIMIT ?""",
            (owner_user_id, contact_id, limit),
        )
        return [dict(row) for row in rows]

    def create_daily_item(self, owner_user_id: str, actor_user_id: str, data: dict[str, Any]) -> dict[str, Any]:
        item_id = f"CRM-WORK-{uuid4().hex}"
        self.database.execute(
            """INSERT INTO crm_daily_items
            (item_id, owner_user_id, actor_user_id, contact_id, item_type, title, details, due_at, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'OPEN')""",
            (item_id, owner_user_id, actor_user_id, data.get("contact_id"),
             data.get("item_type", "TASK"), data["title"], data.get("details", ""), data.get("due_at")),
        )
        self.log_event(owner_user_id, actor_user_id, "DAILY_ITEM_CREATED", data.get("contact_id"),
                       {"item_id": item_id, "title": data["title"], "due_at": data.get("due_at")})
        return self.get_daily_item(owner_user_id, item_id)  # type: ignore[return-value]

    def get_daily_item(self, owner_user_id: str, item_id: str) -> dict[str, Any] | None:
        row = self.database.fetchone(
            "SELECT * FROM crm_daily_items WHERE owner_user_id = ? AND item_id = ?",
            (owner_user_id, item_id),
        )
        return dict(row) if row is not None else None

    def list_daily_items(self, owner_user_id: str, *, status: str | None = None, limit: int = 200) -> list[dict[str, Any]]:
        clauses = ["owner_user_id = ?"]
        params: list[Any] = [owner_user_id]
        if status:
            clauses.append("status = ?")
            params.append(status)
        params.append(limit)
        rows = self.database.fetchall(
            f"SELECT * FROM crm_daily_items WHERE {' AND '.join(clauses)} ORDER BY CASE WHEN due_at IS NULL THEN 1 ELSE 0 END, due_at, created_at DESC LIMIT ?",
            params,
        )
        return [dict(row) for row in rows]

    def update_daily_item(self, owner_user_id: str, actor_user_id: str, item_id: str, status: str) -> dict[str, Any] | None:
        if status not in {"OPEN", "IN_PROGRESS", "DONE", "CANCELLED"}:
            raise ValueError("Unsupported daily item status")
        self.database.execute(
            """UPDATE crm_daily_items SET status = ?, updated_at = CURRENT_TIMESTAMP
               WHERE owner_user_id = ? AND item_id = ?""", (status, owner_user_id, item_id),
        )
        item = self.get_daily_item(owner_user_id, item_id)
        if item is not None:
            self.log_event(owner_user_id, actor_user_id, "DAILY_ITEM_STATUS_CHANGED", item.get("contact_id"),
                           {"item_id": item_id, "status": status})
        return item

    def counts(self, owner_user_id: str) -> dict[str, Any]:
        total = self.database.fetchone("SELECT COUNT(*) AS total FROM crm_contacts WHERE owner_user_id = ?", (owner_user_id,))
        statuses = self.database.fetchall(
            "SELECT contact_status, COUNT(*) AS count FROM crm_contacts WHERE owner_user_id = ? GROUP BY contact_status",
            (owner_user_id,),
        )
        categories = self.database.fetchall(
            "SELECT category, COUNT(*) AS count FROM crm_contacts WHERE owner_user_id = ? GROUP BY category",
            (owner_user_id,),
        )
        overdue = self.database.fetchone(
            """SELECT COUNT(*) AS count FROM crm_contacts WHERE owner_user_id = ?
               AND contact_status = 'ACTIVE' AND follow_up_at IS NOT NULL AND follow_up_at < CURRENT_TIMESTAMP""",
            (owner_user_id,),
        )
        work = self.database.fetchall(
            "SELECT status, COUNT(*) AS count FROM crm_daily_items WHERE owner_user_id = ? GROUP BY status",
            (owner_user_id,),
        )
        return {
            "total_contacts": int(total["total"]) if total else 0,
            "by_status": {row["contact_status"]: int(row["count"]) for row in statuses},
            "by_category": {row["category"]: int(row["count"]) for row in categories},
            "overdue_follow_ups": int(overdue["count"]) if overdue else 0,
            "daily_work_by_status": {row["status"]: int(row["count"]) for row in work},
        }
