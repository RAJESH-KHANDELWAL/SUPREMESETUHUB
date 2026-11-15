"""Email infrastructure controller."""

from __future__ import annotations

from typing import Any

from .model import EmailAccountInfo, EmailServiceInfo
from .service import EmailService


class EmailController:
    """Controller for email infrastructure and SUPREMESETU MAIL."""

    def __init__(self):
        self.service = EmailService()

    # ============================================================
    # EMAIL SERVICE CONFIGURATION
    # ============================================================

    def create(self, info: EmailServiceInfo) -> dict[str, Any]:
        """Create an email service configuration."""
        return self.service.create(info)

    def get(self, email_id: str) -> dict[str, Any] | None:
        """Get an email service configuration."""
        return self.service.get(email_id)

    def list(self) -> list[dict[str, Any]]:
        """List all email service configurations."""
        return self.service.list_all()

    def update_status(
        self,
        email_id: str,
        status: str,
    ) -> dict[str, Any] | None:
        """Update an email service status."""
        return self.service.update_status(
            email_id,
            status,
        )

    def delete(self, email_id: str) -> bool:
        """Delete an email service configuration."""
        return self.service.delete(email_id)

    # ============================================================
    # SUPREMESETU MAIL ACCOUNTS
    # ============================================================

    def create_account(
        self,
        account: EmailAccountInfo,
    ) -> dict[str, Any]:
        """Create a SUPREMESETU MAIL account."""
        return self.service.create_account(account)

    def get_account(
        self,
        account_id: str,
    ) -> dict[str, Any] | None:
        """Get a SUPREMESETU MAIL account."""
        return self.service.get_account(account_id)

    def get_account_by_email(
        self,
        email_address: str,
    ) -> dict[str, Any] | None:
        """Get a SUPREMESETU MAIL account by email address."""
        return self.service.get_account_by_email(
            email_address
        )

    def list_accounts(
        self,
        user_id: str | None = None,
    ) -> list[dict[str, Any]]:
        """List SUPREMESETU MAIL accounts."""
        return self.service.list_accounts(
            user_id=user_id
        )

    def verify_account(
        self,
        account_id: str,
    ) -> dict[str, Any] | None:
        """Verify a SUPREMESETU MAIL account."""
        return self.service.verify_account(
            account_id
        )

    def update_account_status(
        self,
        account_id: str,
        status: str,
    ) -> dict[str, Any] | None:
        """Update a SUPREMESETU MAIL account status."""
        return self.service.update_account_status(
            account_id,
            status,
        )

    def delete_account(
        self,
        account_id: str,
    ) -> bool:
        """Delete a SUPREMESETU MAIL account."""
        return self.service.delete_account(
            account_id
        )
