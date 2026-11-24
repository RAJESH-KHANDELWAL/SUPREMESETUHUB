"""Atlassian Core discovery and orchestration without provider API calls."""
from __future__ import annotations
from typing import Any
from .catalog import get_atlassian_core_catalog
from .domain_catalog import atlassian_domain_summary, list_atlassian_domain_inventory
from .policy import AtlassianCorePolicy
from .product_catalog import atlassian_offerings_summary, list_atlassian_offerings

class AtlassianCoreOrchestrator:
    def catalog(self) -> dict[str, Any]: return get_atlassian_core_catalog()
    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        items = self.catalog()["children"]
        if enabled_only: items = [item for item in items if item.get("enabled", True)]
        return {"success": True, "count": len(items), "products": [AtlassianCorePolicy.safe_module_summary(item) for item in items]}
    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        value = ecosystem_id.strip().casefold()
        for item in self.catalog()["children"]:
            if value and value in (item["ecosystem_id"].casefold(), item["name"].casefold()):
                return AtlassianCorePolicy.safe_module_summary(item)
        return None
    def health(self) -> dict[str, Any]:
        catalog = self.catalog(); domains = atlassian_domain_summary()
        return {"success": True, "ecosystem_id": catalog["ecosystem_id"], "status": "CORE_CATALOG_AVAILABLE", "product_family_count": len(catalog["children"]), "domain_count": domains["domain_count"], "runtime_offering_count": domains["offering_count"], "enabled_product_family_count": sum(bool(item.get("enabled", True)) for item in catalog["children"]), "api_adapter_declared_count": sum(bool(item.get("api_catalog_ref")) for item in catalog["children"]), "live_connections_verified": 0, "api_calls_performed": 0, "warning": "Catalog metadata does not establish Atlassian site authorization, product entitlement or live connectivity."}
    def offerings(self) -> dict[str, Any]: return atlassian_offerings_summary()
    def get_offering(self, product_id: str) -> dict[str, Any] | None:
        return next((item for item in list_atlassian_offerings() if item["id"].casefold() == product_id.strip().casefold()), None)
    def domains(self) -> dict[str, Any]: return atlassian_domain_summary()
    def domain_inventory(self) -> list[dict[str, Any]]: return list_atlassian_domain_inventory()
    def dependency_map(self) -> dict[str, Any]:
        return {"success": True, "edges": [{"core_module": item["core_module"], "api_catalog_ref": item["api_catalog_ref"], "relationship": "DELEGATES_TO_API_LAYER"} for item in self.catalog()["children"]]}
