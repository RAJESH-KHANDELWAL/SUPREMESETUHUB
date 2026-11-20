"""Manager for GLOBAL HOSTING CORE ECOSYSTEM."""
from .catalog import ROOT_ID,get_catalog,list_providers
from .registry import HostingProviderRegistry
class GlobalHostingCoreManager:
 def __init__(self):self.registry=HostingProviderRegistry(get_catalog())
 def status(self):return {"success":True,"ecosystem_id":ROOT_ID,"name":"GLOBAL HOSTING CORE ECOSYSTEM","status":"CORE_CATALOG_ONLY","provider_count":len(list_providers()),"live_connection_verified":False,"api_transport_in_core":False,"persistence_enabled":False}
 def list_providers(self):return {"success":True,"count":len(list_providers()),"providers":list_providers()}
 def get_provider(self,key):return self.registry.get(key)
 def provider_tree(self):
  rows=self.registry.list();root=next((x for x in rows if x["ecosystem_id"]==ROOT_ID),None)
  if root is None:return {"success":False,"tree":None}
  root["children"]=[x for x in rows if x["ecosystem_id"]!=ROOT_ID]
  return {"success":True,"tree":root}
_manager=None
def get_manager():
 global _manager
 if _manager is None:_manager=GlobalHostingCoreManager()
 return _manager
