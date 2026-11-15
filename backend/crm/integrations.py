"""Google integration readiness contract; no OAuth or network calls are performed here."""
from __future__ import annotations

from typing import Any


class GoogleCRMIntegration:
    PROVIDERS = ("GOOGLE_SHEETS", "GOOGLE_CONTACTS")

    def status(self) -> dict[str, Any]:
        return {
            provider: {
                "status": "NOT_CONNECTED",
                "oauth_configured": False,
                "live_api_implemented": False,
                "read_enabled": False,
                "write_enabled": False,
                "sync_enabled": False,
                "next_step": "Configure OAuth securely and test read-only import preview",
            }
            for provider in self.PROVIDERS
        }

    def preview_sync(self, provider: str, records: list[dict[str, Any]]) -> dict[str, Any]:
        provider = provider.strip().upper()
        if provider not in self.PROVIDERS:
            raise ValueError("Unsupported CRM provider")
        if len(records) > 500:
            raise ValueError("A sync preview may contain at most 500 records")
        return {
            "provider": provider,
            "status": "PREVIEW_ONLY",
            "records_received": len(records),
            "records_written": 0,
            "live_connection_required": True,
            "oauth_configured": False,
            "write_enabled": False,
            "human_approval_required": True,
            "note": "This is a validation preview only; no provider API is called and no data is written.",
        }
