"""Apple Core product and domain discovery without Apple API calls."""
from __future__ import annotations
from typing import Any
from .catalog import get_apple_core_catalog
from .domain_catalog import apple_domain_summary,list_apple_domain_inventory
from .policy import AppleCorePolicy
from .product_catalog import apple_offerings_summary,list_apple_offerings
class AppleCoreOrchestrator:
 def catalog(self)->dict[str,Any]:return get_apple_core_catalog()
 def list_products(self,*,enabled_only:bool=False)->dict[str,Any]:
  items=self.catalog()["children"]; items=[x for x in items if x.get("enabled",True)] if enabled_only else items
  return {"success":True,"count":len(items),"products":[AppleCorePolicy.safe_module_summary(x) for x in items]}
 def get_product(self,ecosystem_id:str)->dict[str,Any]|None:
  n=ecosystem_id.strip().casefold()
  return next((AppleCorePolicy.safe_module_summary(x) for x in self.catalog()["children"] if n and (x["ecosystem_id"].casefold()==n or x["name"].casefold()==n)),None)
 def health(self)->dict[str,Any]:
  c=self.catalog();d=apple_domain_summary()
  return {"success":True,"ecosystem_id":c["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","product_family_count":len(c["children"]),"domain_count":d["domain_count"],"runtime_offering_count":d["offering_count"],"enabled_product_family_count":sum(bool(x.get("enabled",True)) for x in c["children"]),"api_adapter_declared_count":sum(bool(x.get("api_catalog_ref")) for x in c["children"]),"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalog metadata does not establish Apple API authorization, entitlements or live connectivity."}
 def offerings(self)->dict[str,Any]:return apple_offerings_summary()
 def get_offering(self,product_id:str)->dict[str,Any]|None:return next((x for x in list_apple_offerings() if x["id"].casefold()==product_id.strip().casefold()),None)
 def domains(self)->dict[str,Any]:return apple_domain_summary()
 def domain_inventory(self)->list[dict[str,Any]]:return list_apple_domain_inventory()
 def dependency_map(self)->dict[str,Any]:return {"success":True,"edges":[{"core_module":x["core_module"],"api_catalog_ref":x["api_catalog_ref"],"relationship":"DELEGATES_TO_API_LAYER"} for x in self.catalog()["children"]]}
