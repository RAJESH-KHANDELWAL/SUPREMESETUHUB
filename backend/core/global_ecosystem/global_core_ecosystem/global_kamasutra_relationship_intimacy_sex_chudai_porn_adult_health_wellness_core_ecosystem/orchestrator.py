"""Read-only product/domain discovery and inventory orchestration."""
from __future__ import annotations

from typing import Any
from .catalog import ECOSYSTEM_ID, get_product, list_products
from .domain_catalog import get_domain, list_domains


class GlobalKamasutraCoreOrchestrator:
    def health(self) -> dict[str, Any]:
        products = list_products()
        return {
            "status": "CATALOG_ONLY",
            "healthy": True,
            "connected": False,
            "domain_count": len(list_domains()),
            "registered_package_count": len(products),
            "enabled_package_count": sum(bool(item.get("enabled")) for item in products),
            "live_connections_verified": 0,
            "api_calls_performed": 0,
        }

    def inventory(self) -> dict[str, Any]:
        products = list_products()
        return {
            "ecosystem_id": ECOSYSTEM_ID,
            "domain_count": len(list_domains()),
            "registered_package_count": len(products),
            "connected_package_count": 0,
            "products": products,
        }

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        return get_product(ecosystem_id)

    def domain_inventory(self) -> list[dict[str, Any]]:
        return [
            {
                **domain,
                "package_count": len(domain["product_ids"]),
                "connected": False,
            }
            for domain in list_domains()
        ]

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return get_domain(domain_id)


__all__ = ["GlobalKamasutraCoreOrchestrator"]
