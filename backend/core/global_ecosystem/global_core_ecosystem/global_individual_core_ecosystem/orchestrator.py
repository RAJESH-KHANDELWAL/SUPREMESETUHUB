"""Discovery, taxonomy and health orchestration for Individual Core."""
from .catalog import ECOSYSTEM,get_catalog,get_capability,list_capabilities
from .policy import GlobalIndividualCorePolicy
class GlobalIndividualCoreOrchestrator:
 def catalog(self):return GlobalIndividualCorePolicy.safe_metadata(get_catalog())
 def list_capabilities(self,enabled_only:bool=False):
  items=list_capabilities(enabled_only)
  return {"success":True,"count":len(items),"capabilities":GlobalIndividualCorePolicy.safe_metadata(items)}
 def get_capability(self,capability_id:str):
  item=get_capability(capability_id)
  return GlobalIndividualCorePolicy.safe_metadata(item) if item else None
 def taxonomy(self):
  domains=sorted({x["domain"] for x in list_capabilities()})
  return {"success":True,"domain_count":len(domains),"domains":domains}
 def health(self):
  return {"success":True,"ecosystem_id":ECOSYSTEM["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","capability_count":len(list_capabilities()),"live_connections_verified":0,"api_calls_performed":0,"api_available":None}
 def dependency_map(self):
  return {"success":True,"edges":[{"capability_id":x["id"],"core_path":x["folder"],"api_adapter_required":True,"live_connection_verified":False,"relationship":"CORE_METADATA_DELEGATES_TO_AUTHORIZED_API_AND_ENGINE_LAYERS"} for x in list_capabilities()]}
__all__=["GlobalIndividualCoreOrchestrator"]
