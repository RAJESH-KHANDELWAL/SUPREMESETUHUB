"""Public Global AI CORE read-only registry service."""
from .catalog import AI_PROVIDERS,ADJACENT_INTEGRATIONS
from .orchestrator import GlobalAICoreOrchestrator
from .policy import GlobalAICorePolicy
class GlobalAICoreEcosystemService:
 NAME="GLOBAL AI CORE ECOSYSTEM"
 def __init__(self): self.orchestrator=GlobalAICoreOrchestrator()
 def status(self): return {"success":True,"ecosystem_id":"GLOBAL-AI-CORE-ECOSYSTEM","name":self.NAME,"status":"CATALOG_AND_CORE_FACADES_REGISTERED","ai_provider_count":len(AI_PROVIDERS),"adjacent_integration_count":len(ADJACENT_INTEGRATIONS),"health":self.orchestrator.health(),**GlobalAICorePolicy.execution_status()}
 def list_providers(self): return self.orchestrator.list_providers()
 def get_provider(self,p): return self.orchestrator.get_provider(p)
 def list_adjacent_integrations(self): return self.orchestrator.list_adjacent_integrations()
 def list_capabilities(self): return self.orchestrator.list_capabilities()
 def list_services(self): return self.orchestrator.list_services()
 def list_tools(self): return self.orchestrator.list_tools()
 def list_integrations(self): return self.orchestrator.list_integrations()
 def dependency_map(self): return self.orchestrator.dependency_map()
