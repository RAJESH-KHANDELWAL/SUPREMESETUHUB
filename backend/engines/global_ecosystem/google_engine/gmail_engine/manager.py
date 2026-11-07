"""Gmail engine facade; delegates API operations to the existing Gmail Core service."""
from __future__ import annotations

from typing import Any

from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem.gmail_core import (
    GoogleGmailCoreService,
)


class GmailEngineManager:
    ENGINE_ID = "GOOGLE-GMAIL-ENGINE"
    NAME = "GOOGLE GMAIL ENGINE"

    def __init__(self, core_service: GoogleGmailCoreService | None = None) -> None:
        self.core_service = core_service or GoogleGmailCoreService()

    def status(self) -> dict[str, Any]:
        result = self.core_service.status()
        return {
            "success": True,
            "engine_id": self.ENGINE_ID,
            "name": self.NAME,
            "core_ecosystem_id": self.core_service.ECOSYSTEM_ID,
            "core_status": result["core_status"],
            "configured": result["api_service"]["configured"],
            "connected": result["connected"],
            "live_connection_verified": False,
        }

    def authorization_url(self) -> dict[str, str]:
        return self.core_service.authorization_url()

    def complete_authorization(self, code: str, state: str, expected_state: str) -> dict[str, Any]:
        return self.core_service.complete_authorization(code, state, expected_state)

    def send_email(self, to: str, subject: str, body: str, *, cc: str | None = None) -> dict[str, str]:
        return self.core_service.send_email(to=to, subject=subject, body=body, cc=cc)
