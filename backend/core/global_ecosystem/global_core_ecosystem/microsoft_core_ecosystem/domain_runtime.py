"""Read-only manager for a registered Microsoft Core domain."""
from __future__ import annotations
from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS, list_microsoft_domain_inventory, microsoft_domain_summary

class MicrosoftCoreDomainManager:
    DOMAIN_ID = ""
    def __init__(self, domain_id: str | None = None) -> None:
        if domain_id is not None:
            self.DOMAIN_ID = domain_id
        if self.DOMAIN_ID not in DOMAIN_DEFINITIONS:
            raise ValueError(f"UNKNOWN_MICROSOFT_CORE_DOMAIN: {self.DOMAIN_ID}")
        self._definition = DOMAIN_DEFINITIONS[self.DOMAIN_ID]

    def status(self) -> dict[str, Any]:
        summary = microsoft_domain_summary()
        item = next(x for x in summary["domains"] if x["domain_id"] == self.DOMAIN_ID)
        return {"success": True, "domain_id": self.DOMAIN_ID, "name": self._definition["name"],
                "purpose": self._definition["purpose"], "status": "CORE_DOMAIN_AVAILABLE",
                "offering_count": item["offering_count"], "live_connections_verified": 0, "api_calls_performed": 0}

    def list_offerings(self) -> dict[str, Any]:
        items = [x for x in list_microsoft_domain_inventory() if x["core_domain_id"] == self.DOMAIN_ID]
        return {"success": True, "domain_id": self.DOMAIN_ID, "count": len(items), "offerings": items}

    def get_offering(self, offering_id: str) -> dict[str, Any] | None:
        needle = offering_id.strip().casefold()
        return next((x for x in list_microsoft_domain_inventory()
                     if x["core_domain_id"] == self.DOMAIN_ID and x["ecosystem_id"].casefold() == needle), None) if needle else None

__all__ = ["MicrosoftCoreDomainManager"]
