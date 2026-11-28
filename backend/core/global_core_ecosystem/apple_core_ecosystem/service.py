"""Apple Core read-only provider control-plane service."""
from __future__ import annotations
from typing import Any
from .catalog import get_apple_core_catalog
from .orchestrator import AppleCoreOrchestrator
class AppleCoreEcosystemService:
 NAME="APPLE CORE ECOSYSTEM"
 def __init__(self)->None:self.orchestrator=AppleCoreOrchestrator()
 def status(self)->dict[str,Any]:
  c=get_apple_core_catalog();h=self.orchestrator.health();r=self.manager_status()
  return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":self.NAME,"provider":"apple","status":c["status"],"registry_status":r["registered"],"module_count":len(c["children"]),"domain_count":h["domain_count"],"runtime_offering_count":h["runtime_offering_count"],"connected_modules":0,"live_connection_verified":False,"api_calls_performed":0,"health":h,"api_catalog_ref":c["api_catalog_ref"]}
 def manager_status(self)->dict[str,Any]:
  try:
   from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
   record=GlobalEcosystemManager().get("GLOBAL-APPLE-CORE-ECOSYSTEM")
  except Exception as exc:return {"success":False,"registered":False,"ecosystem":None,"error":type(exc).__name__}
  return {"success":record is not None,"registered":record is not None,"ecosystem":record,"live_connection_verified":False}
 def list_modules(self):return self.orchestrator.list_products()
 def list_domains(self):return self.orchestrator.domains()
 def list_offerings(self):return self.orchestrator.offerings()
 def get_module(self,ecosystem_id:str):return self.orchestrator.get_product(ecosystem_id)
 def health(self):return self.orchestrator.health()
 def dependency_map(self):return self.orchestrator.dependency_map()
