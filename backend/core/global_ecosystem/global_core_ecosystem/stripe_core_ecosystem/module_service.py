"""Shared read-only implementation for all Stripe product Core managers."""
from .product_catalog import get_stripe_product
from .policy import StripeCorePolicy
class StripeProductCoreService:
 def __init__(self,api_family):self.api_family=api_family
 def metadata(self):
  item=get_stripe_product(self.api_family)
  return StripeCorePolicy.sanitize(item) if item else None
 def status(self):
  item=self.metadata()
  return {"success":item is not None,"provider":"stripe","api_family":self.api_family,"status":item.get("status","NOT_REGISTERED") if item else "NOT_REGISTERED","connected":False,"live_connection_verified":False}
 def capabilities(self):
  item=self.metadata();return list(item.get("capabilities",[])) if item else []
 def validate_capability(self,capability):
  item=get_stripe_product(self.api_family)
  if item is None:raise KeyError("STRIPE_PRODUCT_NOT_REGISTERED")
  StripeCorePolicy.validate_capability(item,capability)
  return {"capability":capability,"classification":StripeCorePolicy.classify_capability(capability),"authorization_performed":"NO"}
def get_product_service(api_family):return StripeProductCoreService(api_family)
