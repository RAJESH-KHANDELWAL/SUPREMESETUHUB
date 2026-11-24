"""AWS Core discovery and orchestration without AWS API calls."""
from __future__ import annotations
from typing import Any
from .catalog import get_aws_core_catalog
from .domain_catalog import aws_domain_summary, list_aws_domain_inventory
from .policy import AwsCorePolicy
from .product_catalog import aws_offerings_summary, list_aws_offerings

class AwsCoreOrchestrator:
    def catalog(self) -> dict[str, Any]:
        return get_aws_core_catalog()
    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        items = self.catalog()["children"]
        if enabled_only:
            items = [item for item in items if item.get("enabled", True)]
        return {"success": True, "count": len(items), "products": [AwsCorePolicy.safe_module_summary(item) for item in items]}
    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        needle = ecosystem_id.strip().casefold()
        if not needle:
            return None
        for item in self.catalog()["children"]:
            if needle in (item["ecosystem_id"].casefold(), item["name"].casefold()):
                return AwsCorePolicy.safe_module_summary(item)
        return None
    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        domains = aws_domain_summary()
        return {"success": True, "ecosystem_id": catalog["ecosystem_id"], "status": "CORE_CATALOG_AVAILABLE", "product_family_count": len(catalog["children"]), "domain_count": domains["domain_count"], "runtime_offering_count": domains["offering_count"], "enabled_product_family_count": sum(bool(x.get("enabled", True)) for x in catalog["children"]), "api_adapter_declared_count": sum(bool(x.get("api_catalog_ref")) for x in catalog["children"]), "live_connections_verified": 0, "api_calls_performed": 0, "warning": "Core catalog does not prove IAM authorization, account access, regional service availability or deployed AWS API connectivity."}
    def offerings(self) -> dict[str, Any]:
        return aws_offerings_summary()
    def get_offering(self, product_id: str) -> dict[str, Any] | None:
        needle = product_id.strip().casefold()
        if not needle:
            return None
        return next((item for item in list_aws_offerings() if item["id"].casefold() == needle), None)
    def domains(self) -> dict[str, Any]:
        return aws_domain_summary()
    def domain_inventory(self) -> list[dict[str, Any]]:
        return list_aws_domain_inventory()
    def dependency_map(self) -> dict[str, Any]:
        return {"success": True, "edges": [{"core_module": item["core_module"], "api_catalog_ref": item["api_catalog_ref"], "relationship": "DELEGATES_TO_API_LAYER"} for item in self.catalog()["children"]]}
