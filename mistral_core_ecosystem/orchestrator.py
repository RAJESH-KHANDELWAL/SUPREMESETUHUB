"""Mistral product/domain discovery and metadata orchestration."""
from __future__ import annotations
from typing import Any
from .catalog import ROOT_ID,get_mistral_core_catalog
from .domain_catalog import mistral_domain_summary,list_mistral_domain_inventory
from .master_catalog import load_master_catalog_summary
from .policy import MistralCorePolicy
from .product_catalog import list_mistral_offerings,mistral_offerings_summary

class MistralCoreOrchestrator:
 def catalog(self)->dict[str,Any]: return get_mistral_core_catalog()
 def list_products(self,*,enabled_only:bool=False)->dict[str,Any]:
  rows=self.catalog()["children"]
  if enabled_only: rows=[x for x in rows if x.get("enabled",True)]
  safe=[MistralCorePolicy.safe_product_summary(x) for x in rows]
  return {"success":True,"count":len(safe),"products":safe}
 def get_product(self,identifier:str)->dict[str,Any]|None:
  needle=identifier.strip().casefold()
  if not needle: return None
  for row in self.catalog()["children"]:
   if needle in {row["key"].casefold(),row["ecosystem_id"].casefold(),row["name"].casefold()}:
    return MistralCorePolicy.safe_product_summary(row)
  return None
 def domains(self)->dict[str,Any]: return mistral_domain_summary()
 def domain_inventory(self)->list[dict[str,Any]]: return list_mistral_domain_inventory()
 def offerings(self)->dict[str,Any]: return mistral_offerings_summary()
 def get_offering(self,offering_id:str)->dict[str,Any]|None:
  key=offering_id.strip().casefold()
  return next((x for x in list_mistral_offerings() if x["id"].casefold()==key),None)
 def master_catalog(self)->dict[str,Any]: return load_master_catalog_summary()
 def health(self)->dict[str,Any]:
  cat=self.catalog();domains=self.domains();master=self.master_catalog();products=cat["children"]
  return {"success":True,"ecosystem_id":ROOT_ID,"status":"CORE_CATALOG_AVAILABLE",
   "product_family_count":len(products),"domain_count":domains["domain_count"],
   "mapped_domain_count":domains["mapped_domain_count"],
   "enabled_product_family_count":sum(bool(x.get("enabled")) for x in products),
   "api_catalog_reference_count":sum(bool(x.get("api_catalog_ref")) for x in products),
   "live_connections_verified":0,"api_calls_performed":0,
   "master_catalog_available":master["available"],
   "master_catalog_target_unique_entries":master["target_unique_entries"],
   "master_catalog_entries_added":0,
   "warning":"Catalog registration does not prove API access, model availability, entitlement or live connectivity."}
 def dependency_map(self)->dict[str,Any]:
  cat=self.catalog();products=cat["children"]
  return {"success":True,"nodes":[{"id":ROOT_ID,"type":"provider_core"}]+
   [{"id":x["ecosystem_id"],"type":"product_core","parent_id":ROOT_ID} for x in products],
   "edges":[{"from":ROOT_ID,"to":x["ecosystem_id"],"relationship":"REGISTERS_METADATA_FOR"} for x in products],
   "layer_dependencies":{"api":cat["api_catalog_ref"],"engine":cat["engine_ref"],
    "runtime":cat["runtime_ref"],"database":"EXTERNAL_SHARED_DATABASE_LAYER",
    "storage":"EXTERNAL_SHARED_STORAGE_LAYER"}}

__all__=["MistralCoreOrchestrator"]
