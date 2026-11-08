"""Independent Gmail CORE metadata service.

CORE owns workflow policy and configuration metadata. It does not import or
instantiate API clients; transport and OAuth execution remain outside CORE.
"""
from __future__ import annotations
from typing import Any

class GoogleGmailCoreService:
    ECOSYSTEM_ID = "GOOGLE-GMAIL-CORE-ECOSYSTEM"
    NAME = "GOOGLE GMAIL CORE ECOSYSTEM"

    def status(self) -> dict[str, Any]:
        return {
            "success": True, "ecosystem_id": self.ECOSYSTEM_ID, "name": self.NAME,
            "provider": "google", "core_status": "READY_FOR_CONFIGURATION",
            "api_client_loaded": False, "connected": False,
            "live_connection_verified": False,
            "boundary": "CORE_METADATA_ONLY",
        }

    def authorization_url(self) -> dict[str, str]:
        return {"success": False, "error": "API_LAYER_REQUIRED",
                "message": "OAuth URL generation is an API-layer responsibility."}

    def complete_authorization(self, code: str, state: str, expected_state: str) -> dict[str, Any]:
        return {"success": False, "error": "API_LAYER_REQUIRED",
                "message": "OAuth callback exchange is an API-layer responsibility."}

    def send_email(self, to: str, subject: str, body: str, *, cc: str | None = None) -> dict[str, str]:
        return {"success": False, "error": "API_LAYER_REQUIRED",
                "message": "Email transport is an API-layer responsibility."}
