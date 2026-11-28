"""Email infrastructure service for SUPREMESETU MAIL."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from backend.database.service import DatabaseService
from backend.infrastructure.email.model import (
    EmailAccountInfo,
    EmailServiceInfo,
)


class EmailService:
    """Central email infrastructure service.

    Handles:
    - Email service configuration
    - SUPREMESETU MAIL accounts
    - Email account verification
    - Email account status management
    """

    def __init__(self, database: Optional[DatabaseService] = None):
        self.database = database or DatabaseService()
        self._ensure_tables()

    # ------------------------------------------------------------------
    # DATABASE INITIALIZATION
    # ------------------------------------------------------------------

    def _ensure_tables(self) -> None:
        """Create required email infrastructure tables."""

        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS email_services (
                email_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email_type TEXT NOT NULL,
                domain TEXT DEFAULT '',
                provider TEXT DEFAULT '',
                smtp_host TEXT DEFAULT '',
                smtp_port INTEGER DEFAULT 0,
                status TEXT DEFAULT 'PLANNED',
                ssl_enabled INTEGER DEFAULT 1,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )

        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS email_accounts (
                account_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                email_address TEXT NOT NULL UNIQUE,
                username TEXT NOT NULL,
                domain TEXT DEFAULT '',
                provider TEXT DEFAULT 'SUPREMESETU',
                account_type TEXT DEFAULT 'MAILBOX',
                status TEXT DEFAULT 'PLANNED',
                verified INTEGER DEFAULT 0,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )

    # ------------------------------------------------------------------
    # EMAIL SERVICE CONFIGURATION
    # ------------------------------------------------------------------

    def create(self, info: EmailServiceInfo) -> Dict[str, Any]:
        """Create an email service configuration."""

        self.database.execute(
            """
            INSERT INTO email_services (
                email_id,
                name,
                email_type,
                domain,
                provider,
                smtp_host,
                smtp_port,
                status,
                ssl_enabled,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                info.email_id,
                info.name,
                info.email_type,
                info.domain,
                info.provider,
                info.smtp_host,
                info.smtp_port,
                info.status,
                int(info.ssl_enabled),
                info.created_at,
                info.updated_at,
            ),
        )

        return info.to_dict()

    def get(self, email_id: str) -> Optional[Dict[str, Any]]:
        """Get an email service configuration by ID."""

        row = self.database.fetch_one(
            """
            SELECT
                email_id,
                name,
                email_type,
                domain,
                provider,
                smtp_host,
                smtp_port,
                status,
                ssl_enabled,
                created_at,
                updated_at
            FROM email_services
            WHERE email_id = ?
            """,
            (email_id,),
        )

        if not row:
            return None

        return dict(row)

    def list_all(self) -> List[Dict[str, Any]]:
        """Return all configured email services."""

        rows = self.database.fetch_all(
            """
            SELECT
                email_id,
                name,
                email_type,
                domain,
                provider,
                smtp_host,
                smtp_port,
                status,
                ssl_enabled,
                created_at,
                updated_at
            FROM email_services
            ORDER BY created_at DESC
            """
        )

        return [dict(row) for row in rows]

    def update_status(
        self,
        email_id: str,
        status: str,
    ) -> Optional[Dict[str, Any]]:
        """Update the status of an email service."""

        updated_at = self._now()

        cursor = self.database.execute(
            """
            UPDATE email_services
            SET status = ?, updated_at = ?
            WHERE email_id = ?
            """,
            (
                status,
                updated_at,
                email_id,
            ),
        )

        if cursor.rowcount == 0:
            return None

        return self.get(email_id)

    def delete(self, email_id: str) -> bool:
        """Delete an email service configuration."""

        cursor = self.database.execute(
            """
            DELETE FROM email_services
            WHERE email_id = ?
            """,
            (email_id,),
        )

        return cursor.rowcount > 0

    # ------------------------------------------------------------------
    # SUPREMESETU MAIL ACCOUNTS
    # ------------------------------------------------------------------

    def create_account(
        self,
        account: EmailAccountInfo,
    ) -> Dict[str, Any]:
        """Create a SUPREMESETU MAIL account."""

        self.database.execute(
            """
            INSERT INTO email_accounts (
                account_id,
                user_id,
                email_address,
                username,
                domain,
                provider,
                account_type,
                status,
                verified,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                account.account_id,
                account.user_id,
                account.email_address,
                account.username,
                account.domain,
                account.provider,
                account.account_type,
                account.status,
                int(account.verified),
                account.created_at,
                account.updated_at,
            ),
        )

        return account.to_dict()

    def get_account(
        self,
        account_id: str,
    ) -> Optional[Dict[str, Any]]:
        """Get a SUPREMESETU MAIL account by account ID."""

        row = self.database.fetch_one(
            """
            SELECT
                account_id,
                user_id,
                email_address,
                username,
                domain,
                provider,
                account_type,
                status,
                verified,
                created_at,
                updated_at
            FROM email_accounts
            WHERE account_id = ?
            """,
            (account_id,),
        )

        if not row:
            return None

        result = dict(row)
        result["verified"] = bool(result.get("verified"))

        return result

    def get_account_by_email(
        self,
        email_address: str,
    ) -> Optional[Dict[str, Any]]:
        """Get a SUPREMESETU MAIL account by email address."""

        row = self.database.fetch_one(
            """
            SELECT
                account_id,
                user_id,
                email_address,
                username,
                domain,
                provider,
                account_type,
                status,
                verified,
                created_at,
                updated_at
            FROM email_accounts
            WHERE email_address = ?
            """,
            (email_address,),
        )

        if not row:
            return None

        result = dict(row)
        result["verified"] = bool(result.get("verified"))

        return result

    def list_accounts(
        self,
        user_id: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """List email accounts.

        If user_id is provided, only that user's accounts are returned.
        Otherwise all accounts are returned.
        """

        if user_id:
            rows = self.database.fetch_all(
                """
                SELECT
                    account_id,
                    user_id,
                    email_address,
                    username,
                    domain,
                    provider,
                    account_type,
                    status,
                    verified,
                    created_at,
                    updated_at
                FROM email_accounts
                WHERE user_id = ?
                ORDER BY created_at DESC
                """,
                (user_id,),
            )
        else:
            rows = self.database.fetch_all(
                """
                SELECT
                    account_id,
                    user_id,
                    email_address,
                    username,
                    domain,
                    provider,
                    account_type,
                    status,
                    verified,
                    created_at,
                    updated_at
                FROM email_accounts
                ORDER BY created_at DESC
                """
            )

        accounts = []

        for row in rows:
            result = dict(row)
            result["verified"] = bool(result.get("verified"))
            accounts.append(result)

        return accounts

    def verify_account(
        self,
        account_id: str,
    ) -> Optional[Dict[str, Any]]:
        """Mark an email account as verified."""

        updated_at = self._now()

        cursor = self.database.execute(
            """
            UPDATE email_accounts
            SET
                verified = 1,
                status = 'ACTIVE',
                updated_at = ?
            WHERE account_id = ?
            """,
            (
                updated_at,
                account_id,
            ),
        )

        if cursor.rowcount == 0:
            return None

        return self.get_account(account_id)

    def update_account_status(
        self,
        account_id: str,
        status: str,
    ) -> Optional[Dict[str, Any]]:
        """Update the status of an email account."""

        updated_at = self._now()

        cursor = self.database.execute(
            """
            UPDATE email_accounts
            SET
                status = ?,
                updated_at = ?
            WHERE account_id = ?
            """,
            (
                status,
                updated_at,
                account_id,
            ),
        )

        if cursor.rowcount == 0:
            return None

        return self.get_account(account_id)

    def delete_account(
        self,
        account_id: str,
    ) -> bool:
        """Delete a SUPREMESETU MAIL account."""

        cursor = self.database.execute(
            """
            DELETE FROM email_accounts
            WHERE account_id = ?
            """,
            (account_id,),
        )

        return cursor.rowcount > 0

    # ------------------------------------------------------------------
    # HELPERS
    # ------------------------------------------------------------------

    @staticmethod
    def _now() -> str:
        """Return the current UTC timestamp."""
        from datetime import datetime, timezone

        return datetime.now(timezone.utc).isoformat()
