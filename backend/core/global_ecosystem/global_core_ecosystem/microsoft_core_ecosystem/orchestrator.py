"""Microsoft Core product discovery and metadata orchestration."""
from __future__ import annotations
from typing import Any
from .catalog import get_microsoft_core_catalog
from .domain_catalog import list_microsoft_domain_inventory,microsoft_domain_summary
from .policy import MicrosoftCorePolicy
class MicrosoftCoreOrchestrator:
    def catalog(self)->dict[str,Any]: return get_microsoft_core_catalog()
    def list_products(self,*,enabled_only:bool=False)->dict[str,Any]:
        items=self.catalog()["children"]
        if enabled_only: items=[x for x in items if x.get("enabled",True)]
        safe=[MicrosoftCorePolicy.safe_module_summary(x) for x in items]
        return {"success":True,"count":len(safe),"products":safe}
    def get_product(self,ecosystem_id:str)->dict[str,Any]|None:
        needle=ecosystem_id.strip().casefold()
        if not needle:return None
        return next((MicrosoftCorePolicy.safe_module_summary(x) for x in self.catalog()["children"] if x["ecosystem_id"].casefold()==needle or x["name"].casefold()==needle),None)
    def domains(self)->dict[str,Any]: return microsoft_domain_summary()
    def domain_inventory(self)->list[dict[str,Any]]: return list_microsoft_domain_inventory()
    def health(self)->dict[str,Any]:
        c=self.catalog(); d=microsoft_domain_summary()
        return {"success":True,"ecosystem_id":c["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","product_family_count":len(c["children"]),"domain_count":d["domain_count"],"registered_product_domain_count":d["assigned_offering_count"],"enabled_product_family_count":sum(bool(x.get("enabled",True)) for x in c["children"]),"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalog readiness is not evidence of deployed adapters, Microsoft tenant authorization, licensing or live connectivity."}
    def dependency_map(self)->dict[str,Any]:
        return {"success":True,"edges":[{"core_module":x["core_module"],"api_catalog_ref":self.catalog().get("api_catalog_ref"),"relationship":"DELEGATES_TO_API_LAYER"} for x in self.catalog()["children"]]}
