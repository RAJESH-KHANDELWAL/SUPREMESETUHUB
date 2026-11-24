"""Shared read-only manager for System Core responsibility domains."""
from __future__ import annotations

from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS
from .product_catalog import list_system_products


class SystemCoreDomainManager:
    def __init__(self, domain_id: str) -> None:
        normalized = domain_id.strip().upper()
        if normalized not in DOMAIN_DEFINITIONS:
            raise LookupError(f"SYSTEM_CORE_DOMAIN_NOT_REGISTERED: {normalized}")
        self.DOMAIN_ID = normalized

    def status(self) -> dict[str, Any]:
        definition = DOMAIN_DEFINITIONS[self.DOMAIN_ID]
        products = self.list_products()["products"]
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "name": definition["name"],
            "purpose": definition["purpose"],
            "product_count": len(products),
            "live_connections_verified": 0,
        }

    def list_products(self) -> dict[str, Any]:
        products = [item for item in list_system_products() if self.DOMAIN_ID in item.get("domain_ids", [])]
        return {"success": True, "domain_id": self.DOMAIN_ID, "count": len(products), "products": products}
