"""Google Core product discovery and lifecycle orchestration."""
from __future__ import annotations

from typing import Any

from .catalog import get_google_core_catalog
from .domain_catalog import google_domain_summary, list_google_domain_inventory
from .policy import GoogleCorePolicy
from .product_catalog import google_offerings_summary, list_google_offerings


class GoogleCoreOrchestrator:
    """Coordinate product and domain metadata without provider API calls."""

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
        domain_summary = google_domain_summary()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            "product_family_count": len(products),
            "domain_count": domain_summary["domain_count"],
            "runtime_offering_count": domain_summary["offering_count"],
            "enabled_product_family_count": sum(bool(p.get("enabled", True)) for p in products),
            "api_adapter_declared_count": sum(bool(p.get("api_catalog_ref")) for p in products),
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "warning": "Catalog and domain readiness are not evidence of deployed adapters or live Google connectivity.",
        }

    def offerings(self) -> dict[str, Any]:
        return google_offerings_summary()

    def get_offering(self, product_id: str) -> dict[str, Any] | None:
        needle = product_id.strip().casefold()
        if not needle:
            return None
        return next((item for item in list_google_offerings() if item["id"].casefold() == needle), None)

    def domains(self) -> dict[str, Any]:
        return google_domain_summary()

    def domain_inventory(self) -> list[dict[str, Any]]:
        return list_google_domain_inventory()

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
