"""API-facing read service for the canonical GLOBAL APP catalog."""
from datetime import datetime, timezone
from backend.global_ecosystem.global_app_ecosystem import (
 list_app_providers,get_app_provider,list_app_types,list_app_capability_groups,get_scope_catalog,
)
class EcosystemService:
 ECOSYSTEM_ID="global-app";ECOSYSTEM_NAME="GLOBAL APP ECOSYSTEM";VERSION="2.0.0"
 def get_status(self):
  providers=list_app_providers()
  return {"success":True,"ecosystem_id":self.ECOSYSTEM_ID,"ecosystem_name":self.ECOSYSTEM_NAME,"version":self.VERSION,
   "status":"catalog_available","implementation_status":"CATALOG_ONLY","live_connection_verified":False,
   "provider_count":len(providers),"app_type_count":len(list_app_types()),"domain_count":len(get_scope_catalog()["domains"]),
   "timestamp":datetime.now(timezone.utc).isoformat()}
 def list_providers(self,*,origin=None,category=None):
  rows=list_app_providers(origin=origin,category=category)
  return {"success":True,"ecosystem_id":self.ECOSYSTEM_ID,"count":len(rows),"providers":list(rows)}
 def get_provider(self,provider_id): return get_app_provider(provider_id)
 def search_providers(self,query):
  term=str(query or "").strip().casefold()
  if not term:return []
  return [x for x in list_app_providers() if term in x["id"] or term in x["name"].casefold() or term in x["application_examples"].casefold()]
 def list_app_types(self): return {"success":True,"count":len(list_app_types()),"app_types":list_app_types()}
 def list_capabilities(self): return {"success":True,"groups":list_app_capability_groups()}
 def list_domains(self): return {"success":True,**get_scope_catalog()}
