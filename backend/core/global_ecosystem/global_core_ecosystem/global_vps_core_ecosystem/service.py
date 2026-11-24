"""Public read-only service facade for Global VPS Core."""
from typing import Any
from .catalog import get_catalog
from .orchestrator import VPSCoreOrchestrator
from .master_catalog import get_master_catalog_mapping
class VPSCoreService:
 def __init__(self)->None:self.orchestrator=VPSCoreOrchestrator()
 def status(self)->dict[str,Any]:
  c=get_catalog();h=self.orchestrator.health();return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":"GLOBAL VPS CORE ECOSYSTEM","status":c["status"],"provider_count":c["provider_count"],"domain_count":h["domain_count"],"connected_provider_count":0,"live_connection_verified":False,"api_transport_in_core":False,"master_catalog":get_master_catalog_mapping(),"health":h}
 def list_providers(self,*,enabled_only:bool=False)->dict[str,Any]:return self.orchestrator.list_providers(enabled_only=enabled_only)
 def get_provider(self,provider_id:str)->dict[str,Any]|None:return self.orchestrator.get_provider(provider_id)
 def list_domains(self)->dict[str,Any]:return self.orchestrator.domains()
 def dependency_map(self)->dict[str,Any]:return self.orchestrator.dependency_map()
 def health(self)->dict[str,Any]:return self.orchestrator.health()
