"""Read-only VPS provider and domain discovery."""
from typing import Any
from .catalog import get_catalog,get_provider
from .domain_catalog import domain_summary,list_domain_inventory
from .policy import safe_provider_summary
class VPSCoreOrchestrator:
 def catalog(self)->dict[str,Any]:return get_catalog()
 def list_providers(self,*,enabled_only:bool=False)->dict[str,Any]:
  items=self.catalog()["providers"];items=[p for p in items if p.get("enabled",True)] if enabled_only else items
  safe=[safe_provider_summary(p) for p in items];return {"success":True,"count":len(safe),"providers":safe}
 def get_provider(self,provider_id:str)->dict[str,Any]|None:
  p=get_provider(provider_id);return safe_provider_summary(p) if p else None
 def domains(self)->dict[str,Any]:return domain_summary()
 def domain_inventory(self)->list[dict[str,str]]:return list_domain_inventory()
 def health(self)->dict[str,Any]:
  c=self.catalog();d=self.domains();return {"success":True,"ecosystem_id":c["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","provider_count":c["provider_count"],"domain_count":d["domain_count"],"enabled_provider_count":sum(bool(p.get("enabled")) for p in c["providers"]),"connected_provider_count":0,"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalogue readiness does not prove provider API availability or live VPS connectivity."}
 def dependency_map(self)->dict[str,Any]:return {"success":True,"edges":[{"provider_id":p["provider_id"],"api_catalog_ref":p["api_catalog_ref"],"relationship":"DELEGATES_TO_GLOBAL_VPS_API_LAYER","provider_api_adapter_verified":False} for p in self.catalog()["providers"]]}
