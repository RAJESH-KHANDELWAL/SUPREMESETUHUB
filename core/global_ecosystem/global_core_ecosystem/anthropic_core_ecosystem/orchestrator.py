"""Anthropic Core product discovery, domain inventory and lifecycle orchestration."""
from __future__ import annotations

from typing import Any

from .catalog import get_anthropic_core_catalog, list_anthropic_core_modules
from .domain_catalog import anthropic_domain_summary, list_anthropic_domain_inventory
from .policy import AnthropicCorePolicy
from .product_catalog import anthropic_offerings_summary, list_anthropic_offerings


class AnthropicCoreOrchestrator:
    """Coordinate Anthropic Core metadata only; no provider API calls."""

    def catalog(self) -> dict[str, Any]:
        return get_anthropic_core_catalog()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        products = list_anthropic_core_modules()
        if enabled_only:
            products = [p for p in products if p.get("enabled", True)]
        safe = [AnthropicCorePolicy.safe_module_summary(p) for p in products]
        return {"success": True, "count": len(safe), "products": safe}

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        needle = ecosystem_id.strip().casefold()
        if not needle:
            return None
        for item in list_anthropic_core_modules():
            if item.get("ecosystem_id", "").casefold() == needle or item.get("name", "").casefold() == needle:
                return AnthropicCorePolicy.safe_module_summary(item)
        return None

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        products = catalog["children"]
        domains = anthropic_domain_summary()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "provider": "anthropic",
            "status": "CORE_CATALOG_AVAILABLE",
            "product_family_count": len(products),
            "domain_count": domains["domain_count"],
            "runtime_offering_count": domains["offering_count"],
            "enabled_product_family_count": sum(bool(p.get("enabled", True)) for p in products),
            "api_adapter_declared_count": sum(bool(p.get("api_catalog_ref")) for p in products),
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "warning": "Core catalog/domain readiness does not prove deployed adapters or live Anthropic connectivity.",
        }

    def offerings(self) -> dict[str, Any]:
        return anthropic_offerings_summary()

    def get_offering(self, product_id: str) -> dict[str, Any] | None:
        needle = product_id.strip().casefold()
        if not needle:
            return None
        return next((item for item in list_anthropic_offerings() if item.get("product_id", "").casefold() == needle or item.get("ecosystem_id", "").casefold() == needle), None)

    def domains(self) -> dict[str, Any]:
        return anthropic_domain_summary()

    def domain_inventory(self) -> list[dict[str, Any]]:
        return list_anthropic_domain_inventory()

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True,
            "edges": [
                {"core_module": item.get("core_module"), "api_catalog_ref": item.get("api_catalog_ref"), "relationship": "DELEGATES_TO_API_LAYER"}
                for item in self.catalog()["children"]
            ],
        }
