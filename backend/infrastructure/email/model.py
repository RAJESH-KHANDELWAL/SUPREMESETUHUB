"""Email infrastructure models for SUPREMESETU MAIL."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class EmailAccountInfo:
    """Canonical email-account identity for SUPREMESETU MAIL."""

    account_id: str
    user_id: str
    email_address: str
    username: str
    domain: str = ""
    provider: str = "SUPREMESETU"
    account_type: str = "MAILBOX"
    status: str = "PLANNED"
    verified: bool = False
    created_at: str = ""
    updated_at: str = ""

    def __post_init__(self) -> None:
        """Populate timestamps when they are not supplied."""
        now = datetime.now(timezone.utc).isoformat()

        if not self.created_at:
            self.created_at = now

        if not self.updated_at:
            self.updated_at = now

    def to_dict(self) -> dict:
        """Return the email account as a dictionary."""
        return {
            "account_id": self.account_id,
            "user_id": self.user_id,
            "email_address": self.email_address,
            "username": self.username,
            "domain": self.domain,
            "provider": self.provider,
            "account_type": self.account_type,
            "status": self.status,
            "verified": self.verified,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


@dataclass
class EmailServiceInfo:
    """Email service configuration.

    This model is retained for backward compatibility with the
    existing SUPREMESETUHUB email infrastructure.
    """

    email_id: str
    name: str
    email_type: str
    domain: str = ""
    provider: str = ""
    smtp_host: str = ""
    smtp_port: int = 0
    status: str = "PLANNED"
    ssl_enabled: bool = True
    created_at: str = ""
    updated_at: str = ""

    def __post_init__(self) -> None:
        """Populate timestamps when they are not supplied."""
        now = datetime.now(timezone.utc).isoformat()

        if not self.created_at:
            self.created_at = now

        if not self.updated_at:
            self.updated_at = now

    def to_dict(self) -> dict:
        """Return the email service configuration as a dictionary."""
        return {
            "email_id": self.email_id,
            "name": self.name,
            "email_type": self.email_type,
            "domain": self.domain,
            "provider": self.provider,
            "smtp_host": self.smtp_host,
            "smtp_port": self.smtp_port,
            "status": self.status,
            "ssl_enabled": self.ssl_enabled,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
