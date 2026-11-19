"""GitHub family discovery and dependency orchestration; no provider calls."""
from .catalog import get_github_core_catalog,list_github_families
from .policy import GitHubCorePolicy
class GitHubCoreOrchestrator:
 def catalog(self): return get_github_core_catalog()
 def list_families(self,enabled_only=False):
  items=list_github_families()
  if enabled_only: items=[x for x in items if x.get("enabled",True)]
  return {"success":True,"count":len(items),"families":[GitHubCorePolicy.safe_summary(x) for x in items]}
 def get_family(self,family):
  needle=str(family).strip().casefold()
  return next((GitHubCorePolicy.safe_summary(x) for x in list_github_families() if x["family"].casefold()==needle or x["name"].casefold()==needle),None)
 def health(self):
  items=list_github_families()
  return {"success":True,"ecosystem_id":"GITHUB-CORE-ECOSYSTEM","status":"CORE_CATALOG_AVAILABLE","family_count":len(items),"families_with_existing_api_routes":sum(bool(x["family_api_routes_implemented"]) for x in items),"live_connections_verified_by_core":0,"api_calls_performed_by_core":0,"warning":"Catalog registration and shared transport do not prove full endpoint coverage or live authentication."}
 def dependency_map(self): return {"success":True,"edges":[{"core_module":x["core_module"],"api_catalog_ref":x["api_catalog_ref"],"api_transport_ref":x["shared_api_transport_ref"],"relationship":"DELEGATES_TO_API_INTEGRATION_LAYER"} for x in list_github_families()]}
