"""Public read-only service contract for the Kamasutra Core ecosystem."""
from __future__ import annotations

from typing import Any
from .catalog import ECOSYSTEM_ID, ECOSYSTEM_NAME, list_products
from .domain_catalog import list_domains
from .policy import get_policy


class GlobalKamasutraCoreService:
    NAME = ECOSYSTEM_NAME

    def status(self) -> dict[str, Any]:
        products = list_products()
        domains = list_domains()
        return {
            "success": True,
            "ecosystem_id": ECOSYSTEM_ID,
            "name": self.NAME,
            "status": "CATALOG_ONLY",
            "enabled": True,
            "connected": False,
            "domain_count": len(domains),
            "registered_package_count": len(products),
            "enabled_package_count": sum(bool(item.get("enabled")) for item in products),
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "policy": get_policy(),
        }


__all__ = ["GlobalKamasutraCoreService"]
