"""Persistent, per-user LINKSETU notification service.

Notifications are stored in the central database. Every read/update operation is
scoped to the recipient so one user cannot mark another user's notifications read.
"""
from __future__ import annotations

from typing import Any
from uuid import uuid4

from backend.database.service import DatabaseService


class LinkSetuNotificationService:
    """Create, list, and mark notifications read for their intended recipient."""

    platform_name = "LINKSETU"
    table_name = "linksetu_notifications"

    def __init__(self, database: DatabaseService | None = None) -> None:
        self.database = database or DatabaseService()
        self.initialize()

    def initialize(self) -> None:
        self.database.execute(
            """CREATE TABLE IF NOT EXISTS linksetu_notifications (
                notification_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                notification_type TEXT NOT NULL,
                message TEXT NOT NULL,
                actor_id TEXT,
                target_id TEXT,
                is_read INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )"""
        )
        self.database.execute(
            """CREATE INDEX IF NOT EXISTS idx_linksetu_notifications_user_created
               ON linksetu_notifications (user_id, created_at DESC)"""
        )

    @staticmethod
    def _as_dict(row: Any) -> dict[str, Any] | None:
        return dict(row) if row is not None else None

    def create_notification(
        self,
        user_id: str,
        notification_type: str,
        message: str,
        actor_id: str | None = None,
        target_id: str | None = None,
    ) -> dict[str, Any]:
        recipient = str(user_id or "").strip()
        kind = str(notification_type or "").strip()
        body = str(message or "").strip()
        if not recipient:
            raise ValueError("user_id is required")
        if not kind:
            raise ValueError("notification_type is required")
        if not body:
            raise ValueError("message is required")

        notification_id = f"NTF-{uuid4().hex}"
        self.database.execute(
            """INSERT INTO linksetu_notifications
               (notification_id, user_id, notification_type, message, actor_id, target_id)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (notification_id, recipient, kind, body, actor_id, target_id),
        )
        row = self.database.fetchone(
            "SELECT * FROM linksetu_notifications WHERE notification_id = ? AND user_id = ?",
            (notification_id, recipient),
        )
        result = self._as_dict(row)
        if result is None:
            raise RuntimeError("Notification was not persisted")
        result["is_read"] = bool(result["is_read"])
        result["platform"] = self.platform_name
        return result

    def get_notifications(self, user_id: str, limit: int = 50) -> dict[str, Any]:
        recipient = str(user_id or "").strip()
        if not recipient:
            raise ValueError("user_id is required")
        safe_limit = max(1, min(int(limit), 200))
        rows = self.database.fetchall(
            """SELECT * FROM linksetu_notifications
               WHERE user_id = ?
               ORDER BY created_at DESC, notification_id DESC
               LIMIT ?""",
            (recipient, safe_limit),
        )
        notifications = []
        for row in rows:
            item = dict(row)
            item["is_read"] = bool(item["is_read"])
            notifications.append(item)
        unread_row = self.database.fetchone(
            "SELECT COUNT(*) AS total FROM linksetu_notifications WHERE user_id = ? AND is_read = 0",
            (recipient,),
        )
        return {
            "platform": self.platform_name,
            "user_id": recipient,
            "notifications": notifications,
            "unread_count": int(unread_row["total"]) if unread_row else 0,
        }

    def mark_as_read(self, notification_id: str, user_id: str) -> dict[str, Any]:
        recipient = str(user_id or "").strip()
        if not recipient:
            raise ValueError("user_id is required")
        cursor = self.database.execute(
            """UPDATE linksetu_notifications SET is_read = 1
               WHERE notification_id = ? AND user_id = ?""",
            (str(notification_id), recipient),
        )
        if cursor.rowcount == 0:
            return {
                "platform": self.platform_name,
                "notification_id": str(notification_id),
                "user_id": recipient,
                "status": "not_found",
            }
        return {
            "platform": self.platform_name,
            "notification_id": str(notification_id),
            "user_id": recipient,
            "status": "read",
        }

    def mark_all_as_read(self, user_id: str) -> dict[str, Any]:
        recipient = str(user_id or "").strip()
        if not recipient:
            raise ValueError("user_id is required")
        cursor = self.database.execute(
            "UPDATE linksetu_notifications SET is_read = 1 WHERE user_id = ? AND is_read = 0",
            (recipient,),
        )
        return {
            "platform": self.platform_name,
            "user_id": recipient,
            "status": "all_read",
            "updated_count": cursor.rowcount,
        }
