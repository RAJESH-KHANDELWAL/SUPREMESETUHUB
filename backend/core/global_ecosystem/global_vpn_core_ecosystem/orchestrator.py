"""Read-only provider and domain discovery for Global VPN Core."""
from typing import Any
from .catalog import get_catalog,get_provider
from .domain_catalog import domain_summary,list_domain_inventory
from .policy import safe_provider_summary
class VPNCoreOrchestrator:
 def catalog(self)->dict[str,Any]:return get_catalog()
 def list_providers(self)->dict[str,Any]:
  items=[safe_provider_summary(p) for p in self.catalog()["providers"]];return {"success":True,"count":len(items),"providers":items}
 def get_provider(self,provider_id:str)->dict[str,Any]|None:
  p=get_provider(provider_id);return safe_provider_summary(p) if p else None
 def domains(self)->dict[str,Any]:return domain_summary()
 def domain_inventory(self)->list[dict[str,str]]:return list_domain_inventory()
 def health(self)->dict[str,Any]:
  c=self.catalog();d=self.domains();return {"success":True,"ecosystem_id":c["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","provider_count":c["provider_count"],"domain_count":d["domain_count"],"configured_provider_count":0,"connected_provider_count":0,"live_connections_verified":0,"tunnel_operations_performed":0,"warning":"Provider catalogue availability is not proof of installed clients or active VPN tunnels."}
 def dependency_map(self)->dict[str,Any]:return {"success":True,"edges":[{"provider_id":p["provider_id"],"source_service_ref":p["source_service_ref"],"relationship":"REFERENCES_EXISTING_VPN_SERVICE_MODULE","live_adapter_verified":False} for p in self.catalog()["providers"]]}
