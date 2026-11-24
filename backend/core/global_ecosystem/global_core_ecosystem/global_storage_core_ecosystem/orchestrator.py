"""Provider/product/domain discovery and dependency metadata."""
from __future__ import annotations
from typing import Any
from .catalog import get_storage_core_catalog,list_storage_providers,get_storage_provider
from .product_catalog import list_storage_products,get_storage_product,storage_product_summary
from .domain_catalog import storage_domain_summary,list_storage_domain_inventory
from .policy import StorageCorePolicy
class GlobalStorageCoreOrchestrator:
 def catalog(self): return get_storage_core_catalog()
 def list_providers(self,*,enabled_only:bool=False)->dict[str,Any]:
  items=[StorageCorePolicy.safe_provider_summary(x) for x in list_storage_providers(enabled_only=enabled_only)]
  return {"success":True,"count":len(items),"providers":items}
 def get_provider(self,provider_id:str):
  item=get_storage_provider(provider_id)
  return StorageCorePolicy.safe_provider_summary(item) if item else None
 def list_products(self,*,provider_id:str|None=None,domain_id:str|None=None,enabled_only:bool=False):
  items=list_storage_products(provider_id=provider_id,domain_id=domain_id,enabled_only=enabled_only)
  return {"success":True,"count":len(items),"products":items}
 def get_product(self,product_id:str): return get_storage_product(product_id)
 def domains(self): return storage_domain_summary()
 def domain_inventory(self): return list_storage_domain_inventory()
 def dependency_map(self):
  c=self.catalog()
  return {"success":True,"edges":[{"provider_id":p["provider_id"],"product_ids":[x["product_id"] for x in c["products"] if x["provider_id"]==p["provider_id"]],"adapter_ref":p["adapter_ref"],"relationship":"DELEGATES_TO_PROVIDER_STORAGE_ADAPTER"} for p in c["providers"]]}
 def health(self):
  c=self.catalog()
  return {"success":True,"ecosystem_id":c["ecosystem_id"],"status":"STORAGE_CORE_CATALOG_AVAILABLE","provider_count":len(c["providers"]),"product_count":len(c["products"]),"domain_count":len(c["domains"]),"configured_adapter_count":sum(bool(p.get("adapter_ref")) for p in c["providers"]),"live_connections_verified":0,"storage_operations_performed":0,"warning":"Catalog metadata does not prove provider credentials, permissions, installation, subscription, entitlement or live connectivity."}
