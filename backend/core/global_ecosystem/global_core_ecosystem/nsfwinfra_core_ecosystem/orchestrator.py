"""Read-only NSFWinfra Core discovery, health and dependency mapping."""
from __future__ import annotations
from typing import Any
from .manager import get_nsfwinfra_core_catalog
from .domain_catalog import get_domain_catalog
class NSFWinfraCoreOrchestrator:
 def products(self,enabled_only:bool=False)->dict[str,Any]:
  rows=get_nsfwinfra_core_catalog()["children"]
  if enabled_only:rows=[x for x in rows if x["enabled"]]
  return {"success":True,"count":len(rows),"products":rows}
 def product(self,ecosystem_id:str)->dict[str,Any]|None:
  return next((p for p in get_nsfwinfra_core_catalog()["children"] if p["ecosystem_id"]==ecosystem_id),None)
 def domains(self)->dict[str,Any]:return {"success":True,"count":len(get_domain_catalog()),"domains":get_domain_catalog()}
 def domain_inventory(self)->list[dict]:return list(get_domain_catalog().values())
 def health(self)->dict:
  catalog=get_nsfwinfra_core_catalog()
  return {"ecosystem_id":catalog["ecosystem_id"],"status":"METADATA_CATALOG_HEALTHY","registered_products":len(catalog["children"]),"domain_count":len(get_domain_catalog()),"connected":False,"live_connection_verified":False,"api_calls_performed":0}
 def offerings(self)->dict[str,Any]:
  rows=get_nsfwinfra_core_catalog()["children"]
  return {"success":True,"count":len(rows),"offerings":[{"id":p["ecosystem_id"],"name":p["name"],"capabilities":p["capabilities"],"domains":p["domains"],"api_reference":p["api_catalog_ref"],"status":p["status"]} for p in rows]}
 def dependency_map(self)->dict[str,Any]:
  c=get_nsfwinfra_core_catalog()
  return {"provider_core":c["core_path"],"api_catalog":c["api_catalog_ref"],"ai_api":c["ai_api_ref"],"ai_core":c["ai_core_ref"],"ai_provider":c["ai_provider_ref"],"database":"SHARED_DATABASE_LAYER_NOT_PROVIDER_OWNED","storage":"SHARED_STORAGE_LAYER_NOT_PROVIDER_OWNED","engine":"NOT_REGISTERED_IN_PROVIDER_ROOT","runtime":"NOT_REGISTERED_IN_PROVIDER_ROOT","master_catalog":"READ_ONLY"}
