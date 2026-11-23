"""Stripe Core metadata discovery and dependency orchestration; no Stripe API calls."""
from .catalog import get_stripe_core_catalog
from .product_catalog import list_stripe_products,get_stripe_product,stripe_product_summary
from .domain_catalog import stripe_domain_summary
from .policy import StripeCorePolicy
class StripeCoreOrchestrator:
 def catalog(self):return get_stripe_core_catalog()
 def list_products(self,*,enabled_only=False):
  items=[StripeCorePolicy.sanitize(p) for p in list_stripe_products(enabled_only=enabled_only)]
  return {"success":True,"count":len(items),"products":items}
 def get_product(self,identifier):
  item=get_stripe_product(identifier);return StripeCorePolicy.sanitize(item) if item else None
 def domains(self):return stripe_domain_summary()
 def health(self):
  products=list_stripe_products()
  return {"success":True,"ecosystem_id":"STRIPE-CORE-ECOSYSTEM","status":"CORE_CATALOG_AVAILABLE","product_family_count":len(products),"domain_count":stripe_domain_summary()["domain_count"],"api_adapter_declared_count":sum(bool(p.get("api_catalog_ref")) for p in products),"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalog presence does not prove merchant eligibility, authorization, deployment or live Stripe connectivity."}
 def offerings(self):return stripe_product_summary()
 def dependency_map(self):return {"success":True,"edges":[{"core_module":p["core_module"],"api_catalog_ref":p["api_catalog_ref"],"relationship":"DELEGATES_TO_API_LAYER"} for p in list_stripe_products()]}
