"""Shared read-only manager for registered Global Cloud Core domains."""
from __future__ import annotations
from typing import Any
from .domain_catalog import CLOUD_DOMAIN_DEFINITIONS, list_cloud_domain_inventory

class GlobalCloudCoreDomainManager:
    DOMAIN_ID = ""

    def __init__(self, domain_id: str | None = None) -> None:
        if domain_id is not None:
            self.DOMAIN_ID = str(domain_id).strip().upper()
        if self.DOMAIN_ID not in CLOUD_DOMAIN_DEFINITIONS:
            raise ValueError(f"UNKNOWN_GLOBAL_CLOUD_CORE_DOMAIN: {self.DOMAIN_ID}")
        self._definition = CLOUD_DOMAIN_DEFINITIONS[self.DOMAIN_ID]

    def status(self) -> dict[str, Any]:
        items = [x for x in list_cloud_domain_inventory() if x["core_domain_id"] == self.DOMAIN_ID]
        return {"success": True, "domain_id": self.DOMAIN_ID, "name": self._definition["name"],
                "purpose": self._definition["purpose"], "status": "CORE_DOMAIN_AVAILABLE",
                "provider_count": len(items), "live_connections_verified": 0, "api_calls_performed": 0}

    def list_products(self) -> dict[str, Any]:
        items = [x for x in list_cloud_domain_inventory() if x["core_domain_id"] == self.DOMAIN_ID]
        return {"success": True, "domain_id": self.DOMAIN_ID, "count": len(items), "products": items}

    def get_product(self, provider_id: str) -> dict[str, Any] | None:
        needle = str(provider_id or "").strip().casefold()
        if not needle:
            return None
        return next((x for x in list_cloud_domain_inventory()
                     if x["core_domain_id"] == self.DOMAIN_ID and x["id"].casefold() == needle), None)

__all__ = ["GlobalCloudCoreDomainManager"]
