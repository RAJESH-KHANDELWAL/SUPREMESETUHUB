"""Provider, product, domain and dependency discovery."""
from .catalog import get_catalog,list_providers,get_provider
from .product_catalog import list_products,get_product
from .domain_catalog import list_domains,domain_summary
from .policy import ToolsCorePolicy
class GlobalToolsCoreOrchestrator:
 def providers(self):
  r=list_providers(); return {"success":True,"count":len(r),"providers":[ToolsCorePolicy.safe_summary(x) for x in r]}
 def products(self,provider_id=None,category=None):
  r=list_products(provider_id,category); return {"success":True,"count":len(r),"products":r}
 def domains(self): return domain_summary()
 def health(self):
  c=get_catalog(); return {"success":True,"ecosystem_id":c["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","provider_count":len(c["providers"]),"product_family_count":len(list_products()),"domain_count":len(list_domains()),"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalogue registration does not prove API availability, entitlement, authorization or live connectivity."}
 def dependency_map(self): return {"success":True,"providers":[{"provider_id":p["provider_id"],"product_count":sum(x["provider_id"]==p["provider_id"] for x in list_products()),"relationship":"OWNS_PRODUCT_METADATA_ONLY"} for p in list_providers()]}
