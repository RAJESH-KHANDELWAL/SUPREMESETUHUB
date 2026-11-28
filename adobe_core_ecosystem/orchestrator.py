"""Adobe Core family discovery and dependency metadata."""
from __future__ import annotations
from typing import Any
from .catalog import get_adobe_core_catalog
from .domain_catalog import adobe_domain_summary, list_adobe_domain_inventory
from .policy import AdobeCorePolicy

class AdobeCoreOrchestrator:
    def catalog(self) -> dict[str, Any]: return get_adobe_core_catalog()
    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        items = self.catalog()["children"]
        if enabled_only: items = [item for item in items if item.get("enabled", True)]
        safe = [AdobeCorePolicy.safe_module_summary(item) for item in items]
        return {"success": True, "count": len(safe), "products": safe}
    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        key = ecosystem_id.strip().casefold()
        if not key: return None
        for item in self.catalog()["children"]:
            if item["ecosystem_id"].casefold() == key or item["name"].casefold() == key:
                return AdobeCorePolicy.safe_module_summary(item)
        return None
    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        products = catalog["children"]
        domains = adobe_domain_summary()
        return {"success": True, "ecosystem_id": catalog["ecosystem_id"],
                "status": "CORE_CATALOG_AVAILABLE", "product_family_count": len(products),
                "domain_count": domains["domain_count"],
                "enabled_product_family_count": sum(bool(p.get("enabled", True)) for p in products),
                "api_adapter_declared_count": sum(bool(p.get("api_catalog_ref")) for p in products),
                "live_connections_verified": 0, "api_calls_performed": 0,
                "warning": "Catalog and domain metadata are not evidence of deployed adapters or live Adobe connectivity."}
    def domains(self) -> dict[str, Any]: return adobe_domain_summary()
    def domain_inventory(self) -> list[dict[str, Any]]: return list_adobe_domain_inventory()
    def dependency_map(self) -> dict[str, Any]:
        return {"success": True, "edges": [{"core_module": item["core_module"],
                "api_catalog_ref": item.get("api_catalog_ref"),
                "relationship": "DELEGATES_TO_API_LAYER"} for item in self.catalog()["children"]]}
