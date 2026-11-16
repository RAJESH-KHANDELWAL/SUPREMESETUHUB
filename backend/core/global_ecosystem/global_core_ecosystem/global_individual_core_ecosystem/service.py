"""Read-only Individual Core catalog service; no provider transport or PII storage."""
from .catalog import ECOSYSTEM,get_catalog,get_capability,list_capabilities
from .policy import GlobalIndividualCorePolicy
class GlobalIndividualCoreService:
 def catalog(self):return GlobalIndividualCorePolicy.safe_metadata(get_catalog())
 def list_capabilities(self,enabled_only:bool=False):
  items=list_capabilities(enabled_only)
  return {"success":True,"count":len(items),"capabilities":GlobalIndividualCorePolicy.safe_metadata(items)}
 def get_capability(self,capability_id:str):
  item=get_capability(capability_id)
  return GlobalIndividualCorePolicy.safe_metadata(item) if item else None
 def health(self):
  items=list_capabilities()
  return {"success":True,"ecosystem_id":ECOSYSTEM["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","capability_count":len(items),"enabled_capability_count":sum(bool(x.get("enabled",True)) for x in items),"api_available":None,"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalog registration is not evidence of provider connectivity or authorization."}
__all__=["GlobalIndividualCoreService"]
