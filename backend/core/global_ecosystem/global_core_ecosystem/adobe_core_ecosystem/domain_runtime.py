"""Read-only shared runtime for Adobe Core domain/product-family managers."""
from __future__ import annotations
from typing import Any
from .domain_catalog import list_adobe_domain_inventory, adobe_domain_summary

class AdobeCoreDomainManager:
    """Discovery facade for a registered Adobe domain; performs no provider I/O."""
    DOMAIN_ID = ""
    def __init__(self, domain_id: str | None = None) -> None:
        if domain_id is not None:
            self.DOMAIN_ID = domain_id.strip().upper()
        inventory = list_adobe_domain_inventory()
        self._domain = next((item for item in inventory if item["domain_id"] == self.DOMAIN_ID), None)
        if self._domain is None:
            raise ValueError(f"UNKNOWN_ADOBE_CORE_DOMAIN: {self.DOMAIN_ID}")
    def status(self) -> dict[str, Any]:
        summary = adobe_domain_summary()
        item = next(domain for domain in summary["domains"] if domain["domain_id"] == self.DOMAIN_ID)
        return {"success": True, **item, "status": "CORE_DOMAIN_AVAILABLE",
                "live_connections_verified": 0, "api_calls_performed": 0}
    def list_offerings(self) -> dict[str, Any]:
        if self.DOMAIN_ID == "PROVIDER_GOVERNANCE":
            return {"success": True, "domain_id": self.DOMAIN_ID, "count": 1,
                    "offerings": [{"id": "ADOBE-CORE-ECOSYSTEM", "name": "ADOBE CORE ECOSYSTEM",
                                  "provider": "adobe", "status": "CORE_CATALOG_AVAILABLE"}]}
        catalog = __import__("backend.core.global_ecosystem.global_core_ecosystem.adobe_core_ecosystem.catalog", fromlist=["get_adobe_core_catalog"])
        items = [item for item in catalog.get_adobe_core_catalog()["children"]
                 if item["product_key"].upper() == self.DOMAIN_ID]
        return {"success": True, "domain_id": self.DOMAIN_ID, "count": len(items), "offerings": items}
    def get_offering(self, offering_id: str) -> dict[str, Any] | None:
        needle = offering_id.strip().casefold()
        return next((item for item in self.list_offerings()["offerings"]
                    if item.get("ecosystem_id", item.get("id", "")).casefold() == needle
                    or item.get("product_key", "").casefold() == needle), None)

__all__ = ["AdobeCoreDomainManager"]
