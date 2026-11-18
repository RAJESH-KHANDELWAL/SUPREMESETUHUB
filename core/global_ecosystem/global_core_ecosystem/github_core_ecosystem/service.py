"""GitHub provider-level CORE ecosystem read-only service."""
from .catalog import get_github_core_catalog
from .orchestrator import GitHubCoreOrchestrator
class GitHubCoreEcosystemService:
 def __init__(self): self.orchestrator=GitHubCoreOrchestrator()
 def status(self):
  c=get_github_core_catalog(); h=self.orchestrator.health()
  return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":c["name"],"provider":"github","status":c["status"],"family_count":len(c["children"]),"live_connection_verified":False,"api_calls_performed_by_core":0,"api_catalog_ref":c["api_catalog_ref"],"api_transport_ref":c["api_transport_ref"],"api_routes_ref":c["api_routes_ref"],"health":h,"live_connection_check_owner":"API route GET /api/v1/connectors/github/status"}
 def list_families(self): return self.orchestrator.list_families()
 def get_family(self,family): return self.orchestrator.get_family(family)
 def health(self): return self.orchestrator.health()
 def dependency_map(self): return self.orchestrator.dependency_map()
