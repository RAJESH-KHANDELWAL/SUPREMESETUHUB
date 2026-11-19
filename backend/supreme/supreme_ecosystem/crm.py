"""CRM Ecosystem integration point owned by SUPREME ECOSYSTEM.

The CRM domain model lives in backend.crm. This module coordinates ecosystem
readiness only; it does not claim that Google providers are connected.
"""
from __future__ import annotations

from typing import Any

from backend.crm.contact_service import ContactService


class CRMEcosystem:
    NAME = "CRM_ECOSYSTEM"
    PROVIDERS = ("GOOGLE_CONTACTS", "GOOGLE_SHEETS")

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            "ecosystem": self.NAME,
            "crm_module": "backend.crm",
            "private_owner_crm": "SEPARATE_MODULE_AND_DATA_BOUNDARY",
            "providers": {
                provider: {
                    "status": "NOT_CONNECTED",
                    "sync_enabled": False,
                    "live_api_implemented": False,
                }
                for provider in self.PROVIDERS
            },
        }

    @staticmethod
    def contact_service() -> ContactService:
        """Return the CRM's provider-neutral contact normalization service."""
        return ContactService()
