"""Google Core product discovery and lifecycle orchestration."""
from __future__ import annotations

from typing import Any

from .catalog import get_google_core_catalog
from .policy import GoogleCorePolicy


class GoogleCoreOrchestrator:
    """Coordinate product Core metadata without executing provider API calls."""

    def catalog(self) -> dict[str, Any]:
        return get_google_core_catalog()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        children = self.catalog()["children"]
        if enabled_only:
            children = [item for item in children if item.get("enabled", True)]
        safe = [GoogleCorePolicy.safe_module_summary(item) for item in children]
        return {"success": True, "count": len(safe), "products": safe}

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        needle = ecosystem_id.strip().casefold()
        if not needle:
            return None
        for item in self.catalog()["children"]:
            if item["ecosystem_id"].casefold() == needle or item["name"].casefold() == needle:
                return GoogleCorePolicy.safe_module_summary(item)
        return None

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        products = catalog["children"]
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            "product_count": len(products),
            "enabled_count": sum(bool(p.get("enabled", True)) for p in products),
            "api_adapter_declared_count": sum(bool(p.get("api_catalog_ref")) for p in products),
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "warning": "Catalog readiness is not evidence of deployed adapters or live Google connectivity.",
        }

    def dependency_map(self) -> dict[str, Any]:
        products = self.catalog()["children"]
        return {
            "success": True,
            "edges": [
                {
                    "core_module": item["core_module"],
                    "api_catalog_ref": item.get("api_catalog_ref"),
                    "relationship": "DELEGATES_TO_API_LAYER",
                }
                for item in products
            ],
        }
