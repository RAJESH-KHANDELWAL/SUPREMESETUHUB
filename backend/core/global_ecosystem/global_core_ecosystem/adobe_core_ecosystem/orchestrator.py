"""Adobe Core family discovery and dependency metadata."""
from __future__ import annotations
from typing import Any
from .catalog import get_adobe_core_catalog
from .policy import AdobeCorePolicy
class AdobeCoreOrchestrator:
    def catalog(self) -> dict[str,Any]: return get_adobe_core_catalog()
    def list_products(self, enabled_only: bool=False) -> dict[str,Any]:
        items=self.catalog()["children"]
        if enabled_only: items=[x for x in items if x.get("enabled",True)]
        return {"success":True,"count":len(items),"products":[AdobeCorePolicy.safe_module_summary(x) for x in items]}
    def get_product(self, ecosystem_id: str) -> dict[str,Any] | None:
        key=ecosystem_id.strip().casefold()
        for item in self.catalog()["children"]:
            if item["ecosystem_id"].casefold()==key or item["name"].casefold()==key:
                return AdobeCorePolicy.safe_module_summary(item)
        return None
    def health(self) -> dict[str,Any]:
        items=self.catalog()["children"]
        return {"success":True,"ecosystem_id":"ADOBE-CORE-ECOSYSTEM","status":"CORE_CATALOG_AVAILABLE",
                "product_family_count":len(items),"enabled_product_family_count":sum(bool(x.get("enabled",True)) for x in items),
                "live_connections_verified":0,"api_calls_performed":0,
                "warning":"Catalog metadata is not evidence of deployed adapters or live Adobe connectivity."}
    def dependency_map(self) -> dict[str,Any]:
        return {"success":True,"edges":[{"core_module":x["core_module"],"api_catalog_ref":x.get("api_catalog_ref"),
                "relationship":"DELEGATES_TO_API_LAYER"} for x in self.catalog()["children"]]}
