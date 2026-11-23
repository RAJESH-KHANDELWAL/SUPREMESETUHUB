"""Stripe Core metadata guardrails; authorization is performed in the API/application layer."""
from typing import Any
SENSITIVE_MARKERS=("PAYMENT","PAYOUT","REFUND","DELETE","WRITE","ISSUING","TREASURY","TAX","DISPUTE","ADMIN")
BLOCKED_KEYS={"token","access_token","refresh_token","client_secret","secret_key","api_key","authorization","pan","cvc","card_number"}
class StripeCorePolicyError(PermissionError):pass
class StripeCorePolicy:
 @staticmethod
 def require_tenant_context(context:Any):
  if context is None or not callable(getattr(context,"validate",None)):raise StripeCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
  context.validate()
 @staticmethod
 def validate_capability(product:dict[str,Any],capability:str):
  if not product.get("enabled",True):raise StripeCorePolicyError("PRODUCT_DISABLED")
  if capability not in set(product.get("capabilities",[])):raise StripeCorePolicyError("CAPABILITY_NOT_REGISTERED")
 @staticmethod
 def classify_capability(capability:str):
  return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION_AND_AUDIT" if any(x in capability.upper() for x in SENSITIVE_MARKERS) else "TENANT_AUTHORIZATION_REQUIRED"
 @staticmethod
 def sanitize(value:Any):
  if isinstance(value,dict):return {k:StripeCorePolicy.sanitize(v) for k,v in value.items() if k.casefold() not in BLOCKED_KEYS}
  if isinstance(value,(list,tuple)):return [StripeCorePolicy.sanitize(v) for v in value]
  return value
