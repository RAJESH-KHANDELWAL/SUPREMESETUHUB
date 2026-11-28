"""Slack Core policy guardrails; capability metadata never grants API access."""
from typing import Any
SENSITIVE=("ADMIN","DELETE","WRITE","SEND","UPLOAD","SHARE","OAUTH","WORKFLOW","ARCHIVE")
BLOCKED={"token","access_token","refresh_token","client_secret","api_key","secret","authorization","password","signing_secret"}
class SlackCorePolicyError(PermissionError):pass
class SlackCorePolicy:
 @staticmethod
 def require_tenant_context(context:Any):
  if context is None:raise SlackCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
  validator=getattr(context,"validate",None)
  if not callable(validator):raise SlackCorePolicyError("INVALID_TENANT_CONTEXT")
  validator()
 @staticmethod
 def validate_capability(product,capability):
  if not product.get("enabled",True):raise SlackCorePolicyError("PRODUCT_DISABLED")
  if capability not in set(product.get("capabilities",[])):raise SlackCorePolicyError("CAPABILITY_NOT_REGISTERED")
 @staticmethod
 def classify_capability(capability):return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(x in capability.upper() for x in SENSITIVE) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
 @staticmethod
 def safe_metadata(value):
  if isinstance(value,dict):return {k:SlackCorePolicy.safe_metadata(v) for k,v in value.items() if str(k).casefold() not in BLOCKED}
  if isinstance(value,list):return [SlackCorePolicy.safe_metadata(v) for v in value]
  return value
