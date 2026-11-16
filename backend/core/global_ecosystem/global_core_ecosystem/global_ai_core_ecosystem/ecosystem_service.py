"""Global AI Core read-only provider registry service."""
from .catalog import ECOSYSTEM
from .orchestrator import GlobalAICoreOrchestrator
class GlobalAICoreEcosystemService:
 NAME="GLOBAL AI CORE ECOSYSTEM"
 def __init__(self):self.orchestrator=GlobalAICoreOrchestrator()
 def status(self):
  h=self.orchestrator.health();m=self.manager_status()
  return {"success":True,"ecosystem_id":ECOSYSTEM["ecosystem_id"],"name":self.NAME,"provider":"global_ai","status":ECOSYSTEM["status"],"registry_status":m["registered"],"module_count":h["provider_count"],"domain_count":h["domain_count"],"runtime_offering_count":h["runtime_offering_count"],"connected_modules":0,"live_connection_verified":False,"api_calls_performed":0,"health":h}
 def list_modules(self):return self.orchestrator.list_products()
 def list_domains(self):return self.orchestrator.domains()
 def list_offerings(self):return self.orchestrator.offerings()
 def manager_status(self):
  try:
   from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
   record=GlobalEcosystemManager().get("GLOBAL-AI-CORE-ECOSYSTEM")
  except Exception as exc:return {"success":False,"registered":False,"ecosystem":None,"error":type(exc).__name__}
  return {"success":record is not None,"registered":record is not None,"ecosystem":record,"live_connection_verified":False}
 def get_module(self,provider_id):return self.orchestrator.get_product(provider_id)
 def health(self):return self.orchestrator.health()
 def dependency_map(self):return self.orchestrator.dependency_map()
