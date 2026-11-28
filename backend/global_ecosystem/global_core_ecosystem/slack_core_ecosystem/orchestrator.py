"""Slack Core discovery, domain and dependency orchestration."""
from .catalog import get_slack_core_catalog
from .domain_catalog import domain_summary,list_domain_inventory
from .policy import SlackCorePolicy
from .product_catalog import list_products,get_product
class SlackCoreOrchestrator:
 def catalog(self):return get_slack_core_catalog()
 def list_products(self,*,enabled_only=False):
  items=[SlackCorePolicy.safe_metadata(x) for x in list_products(enabled_only=enabled_only)];return {"success":True,"count":len(items),"products":items}
 def get_product(self,identifier):
  x=get_product(identifier);return SlackCorePolicy.safe_metadata(x) if x else None
 def domains(self):return domain_summary()
 def domain_inventory(self):return list_domain_inventory()
 def dependency_map(self):return {"success":True,"edges":[{"ecosystem_id":p["ecosystem_id"],"api_catalog_ref":get_slack_core_catalog()["api_catalog_ref"],"relationship":"DELEGATES_TO_SLACK_API_LAYER","transport_in_core":False} for p in list_products()]}
 def health(self):
  c=self.catalog();d=self.domains()
  return {"success":True,"ecosystem_id":c["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","product_count":len(c["children"]),"enabled_product_count":sum(bool(x["enabled"]) for x in c["children"]),"domain_count":d["domain_count"],"capability_count":sum(len(x["capabilities"]) for x in c["children"]),"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalog metadata does not prove Slack app installation, OAuth grants, workspace entitlement or live connectivity."}
