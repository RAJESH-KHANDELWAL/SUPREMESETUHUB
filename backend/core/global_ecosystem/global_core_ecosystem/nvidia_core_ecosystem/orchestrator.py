from .catalog import get_catalog
from .product_catalog import list_products,get_product
from .domain_catalog import list_domains
from .policy import safe_summary
class NvidiaCoreOrchestrator:
 def catalog(self):return get_catalog()
 def products(self,enabled_only=False):
  p=list_products();p=[x for x in p if x["enabled"]] if enabled_only else p;return {"success":True,"count":len(p),"products":[safe_summary(x) for x in p]}
 def product(self,k):return get_product(k)
 def domains(self):return {"success":True,"count":len(list_domains()),"domains":list_domains()}
 def health(self):
  c=self.catalog();return {"success":True,"status":"CORE_CATALOG_AVAILABLE","product_count":c["product_count"],"domain_count":c["domain_count"],"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalog presence is not account, license, hardware, deployment or live API verification."}
 def dependency_map(self):return {"success":True,"edges":[{"product_id":p["product_id"],"api_ref":p["api_catalog_ref"],"engine_ref":p["engine_ref"],"relationship":"LAYER_DELEGATION"} for p in list_products()]}
