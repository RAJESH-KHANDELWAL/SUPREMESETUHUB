"""Developer Core discovery and lifecycle metadata orchestration."""
from __future__ import annotations
from typing import Any
from .manager import get_global_developer_core_catalog
from .domain_catalog import developer_domain_summary, list_developer_domain_inventory
from .policy import DeveloperCorePolicy

class DeveloperCoreOrchestrator:
    def catalog(self) -> dict[str,Any]: return get_global_developer_core_catalog()
    def list_products(self, *, enabled_only: bool=False) -> dict[str,Any]:
        items=self.catalog()["children"]
        if enabled_only: items=[x for x in items if x.get("enabled",True)]
        safe=[DeveloperCorePolicy.safe_module_summary(x) for x in items]
        return {"success":True,"count":len(safe),"products":safe}
    def get_product(self, ecosystem_id: str) -> dict[str,Any] | None:
        needle=ecosystem_id.strip().casefold()
        if not needle:return None
        return next((DeveloperCorePolicy.safe_module_summary(x) for x in self.catalog()["children"] if x["ecosystem_id"].casefold()==needle or x["name"].casefold()==needle),None)
    def domains(self) -> dict[str,Any]: return developer_domain_summary()
    def domain_inventory(self) -> list[dict[str,Any]]: return list_developer_domain_inventory()
    def health(self) -> dict[str,Any]:
        c=self.catalog();items=c["children"];d=developer_domain_summary()
        return {"success":True,"ecosystem_id":c["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","product_family_count":len(items),"domain_count":d["domain_count"],"enabled_product_family_count":sum(bool(x.get("enabled",True)) for x in items),"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalog metadata is not evidence of provider API access, deployment or live connectivity."}
    def dependency_map(self) -> dict[str,Any]:
        return {"success":True,"edges":[{"core_module":x["core_module"],"api_catalog_ref":x.get("api_catalog_ref"),"relationship":"DELEGATES_TO_API_LAYER"} for x in self.catalog()["children"]]}
