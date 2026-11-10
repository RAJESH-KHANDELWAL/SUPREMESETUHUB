"""CORE-owned application ecosystem selection and validation.

CORE defines use-case decisions and contracts. It does not expose HTTP routes,
run provider adapters, or persist records.
"""
from backend.global_ecosystem.global_app_ecosystem import get_app_provider,list_app_types,get_scope_catalog
class GlobalAppCoreService:
 def resolve_provider(self,provider_id:str):
  provider=get_app_provider(provider_id)
  if provider is None: raise KeyError(f"Unknown APP provider: {provider_id}")
  return provider
 def validate_app_type(self,app_type_id:str):
  for item in list_app_types():
   if item["id"]==app_type_id:return item
  raise KeyError(f"Unknown APP type: {app_type_id}")
 def catalog_snapshot(self):
  return {"layer":"CORE","ecosystem":"GLOBAL_APP_ECOSYSTEM","provider_count":len(__import__("backend.global_ecosystem.global_app_ecosystem",fromlist=["list_app_providers"]).list_app_providers()),"domains":get_scope_catalog()["domains"],"execution":"NOT_PERFORMED","persistence":"NOT_PERFORMED"}
__all__=["GlobalAppCoreService"]
