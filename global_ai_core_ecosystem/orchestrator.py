"""Global AI product/domain discovery and health orchestration."""
from .catalog import ECOSYSTEM,list_ai_providers,get_ai_provider,get_global_ai_catalog
from .domain_catalog import ai_domain_summary,list_ai_domain_inventory
from .product_catalog import ai_offerings_summary,list_ai_offerings
class GlobalAICoreOrchestrator:
 def catalog(self):return get_global_ai_catalog()
 def list_products(self,enabled_only=False):
  x=list_ai_providers()
  if enabled_only:x=[p for p in x if p.get("enabled",True)]
  return {"success":True,"count":len(x),"products":x}
 def get_product(self,provider_id):return get_ai_provider(provider_id)
 def domains(self):return ai_domain_summary()
 def domain_inventory(self):return list_ai_domain_inventory()
 def offerings(self):return ai_offerings_summary()
 def get_offering(self,provider_id):return next((x for x in list_ai_offerings() if x["id"]==provider_id),None)
 def health(self):
  p=list_ai_providers();d=ai_domain_summary()
  return {"success":True,"ecosystem_id":ECOSYSTEM["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","provider_count":len(p),"domain_count":d["domain_count"],"active_domain_count":d["active_domain_count"],"runtime_offering_count":len(p),"catalog_only_count":sum(x["integration_status"]=="catalog_only" for x in p),"adapter_scaffold_count":sum(x["integration_status"]=="scaffold" for x in p),"integration_in_progress_count":sum(x["integration_status"]=="integration_in_progress" for x in p),"live_provider_count":sum(x["integration_status"]=="live" for x in p),"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalog readiness is not evidence of live provider connectivity."}
 def dependency_map(self):return {"success":True,"edges":[{"core_module":x["core_module"],"runtime_module":x["runtime_module"],"api_endpoint_declared":bool(x.get("api_endpoint")),"relationship":"DELEGATES_TO_RUNTIME_AND_API"} for x in list_ai_providers()]}
