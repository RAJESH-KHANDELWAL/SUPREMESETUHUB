"""Meta Core product/domain discovery, health and dependency orchestration."""
from __future__ import annotations
from typing import Any
from .catalog import get_meta_core_catalog
from .product_catalog import list_meta_products,get_meta_product
from .domain_catalog import list_meta_domain_inventory,meta_domain_summary
from .policy import MetaCorePolicy
class MetaCoreOrchestrator:
    def catalog(self)->dict[str,Any]: return get_meta_core_catalog()
    def list_products(self,*,enabled_only:bool=False)->dict[str,Any]:
        items=list_meta_products()
        if enabled_only: items=[x for x in items if x.get("enabled",True)]
        return {"success":True,"count":len(items),"products":[MetaCorePolicy.sanitize(x) for x in items]}
    def get_product(self,product_id:str)->dict[str,Any]|None:
        item=get_meta_product(product_id)
        return MetaCorePolicy.sanitize(item) if item else None
    def domains(self)->dict[str,Any]:
        items=list_meta_domain_inventory()
        return {"success":True,**meta_domain_summary(),"domains":items}
    def domain_inventory(self)->list[dict[str,Any]]: return list_meta_domain_inventory()
    def health(self)->dict[str,Any]:
        catalog=self.catalog(); products=catalog["children"]; domains=catalog["domains"]
        return {"success":True,"ecosystem_id":catalog["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","product_family_count":len(products),"domain_count":len(domains),"enabled_product_family_count":sum(bool(x["enabled"]) for x in products),"api_catalog_family_count":len(products),"engine_boundary_declared_count":sum(bool(x["engine_module"]) for x in products),"discovery_only_product_count":sum(x["status"]=="DISCOVERY_ONLY" for x in products),"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalog presence and app configuration do not prove Meta app review, permissions, asset eligibility or live API connectivity."}
    def dependency_map(self)->dict[str,Any]:
        return {"success":True,"edges":[{"core_module":x["core_module"],"api_module":x["api_module"],"engine_module":x["engine_module"],"relationship":"CORE_METADATA_DELEGATES_API_TRANSPORT_AND_ENGINE_EXECUTION"} for x in list_meta_products()]}
