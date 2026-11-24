"""Shared read-only runtime for Apple Core responsibility domains."""
from __future__ import annotations
from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS, PRODUCT_DOMAIN
from .product_catalog import list_apple_offerings

class AppleCoreDomainManager:
    """Domain-scoped discovery manager; no Apple API calls or authorization."""
    DOMAIN_ID = ""
    def __init__(self, domain_id: str | None = None) -> None:
        if domain_id is not None:
            self.DOMAIN_ID = domain_id
        if self.DOMAIN_ID not in DOMAIN_DEFINITIONS:
            raise ValueError(f"UNKNOWN_APPLE_CORE_DOMAIN: {self.DOMAIN_ID}")
        self._definition = DOMAIN_DEFINITIONS[self.DOMAIN_ID]
    def status(self) -> dict[str, Any]:
        items = self.list_offerings()["offerings"]
        return {"success": True, "domain_id": self.DOMAIN_ID,
                "name": self._definition["name"], "purpose": self._definition["purpose"],
                "status": "CORE_DOMAIN_AVAILABLE", "offering_count": len(items),
                "live_connections_verified": 0, "api_calls_performed": 0}
    def list_offerings(self) -> dict[str, Any]:
        items = [item for item in list_apple_offerings()
                 if PRODUCT_DOMAIN.get(item["id"]) == self.DOMAIN_ID]
        return {"success": True, "domain_id": self.DOMAIN_ID, "count": len(items), "offerings": items}
    def get_offering(self, offering_id: str) -> dict[str, Any] | None:
        needle = offering_id.strip().casefold()
        if not needle: return None
        return next((item for item in self.list_offerings()["offerings"]
                    if item["id"].casefold() == needle), None)
__all__ = ["AppleCoreDomainManager"]
