"""Public core facade for Google Gmail; delegates to the existing Gmail API service."""
from __future__ import annotations

from typing import Any

from backend.api.global_ecosystem.global_api_ecosystem.google_api_ecosystem.google_gmail_api_ecosystem.service import (
    GmailAPIService,
)


class GoogleGmailCoreService:
    """Core facade; the API adapter remains the single Gmail client implementation."""

    ECOSYSTEM_ID = "GOOGLE-GMAIL-CORE-ECOSYSTEM"
    NAME = "GOOGLE GMAIL CORE ECOSYSTEM"

    def __init__(self, api_service: GmailAPIService | None = None) -> None:
        self.api_service = api_service or GmailAPIService()

    def status(self) -> dict[str, Any]:
        api_status = self.api_service.status()
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "name": self.NAME,
            "provider": "google",
            "api_service": api_status,
            "core_status": "READY_FOR_CONFIGURATION" if api_status["configured"] else "NEEDS_CONFIGURATION",
            "connected": bool(api_status["connected"]),
            "live_connection_verified": False,
        }

    def authorization_url(self) -> dict[str, str]:
        return self.api_service.authorization_url()

    def complete_authorization(self, code: str, state: str, expected_state: str) -> dict[str, Any]:
        return self.api_service.complete_authorization(code, state, expected_state)

    def send_email(self, to: str, subject: str, body: str, *, cc: str | None = None) -> dict[str, str]:
        return self.api_service.send_email(to=to, subject=subject, body=body, cc=cc)
