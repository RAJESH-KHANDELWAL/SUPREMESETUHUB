"""Metadata-only safety and tenant policy checks."""
from __future__ import annotations
from typing import Any
SENSITIVE_MARKERS=("ADMIN","DELETE","WRITE","UPLOAD","PUBLISH","BILLING","WEBHOOK","SIGN","GENERATE","EDIT","VIDEO","IMAGE","ANIME","ADULT","NSFW")
class NSFWinfraCorePolicyError(PermissionError):pass
class NSFWinfraCorePolicy:
 @staticmethod
 def require_tenant_context(context:Any)->None:
  if context is None:raise NSFWinfraCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
  validator=getattr(context,"validate",None)
  if not callable(validator):raise NSFWinfraCorePolicyError("INVALID_TENANT_CONTEXT")
  validator()
 @staticmethod
 def validate_capability(product:dict[str,Any],capability:str)->None:
  if not product.get("enabled",True):raise NSFWinfraCorePolicyError("PRODUCT_DISABLED")
  if capability not in product.get("capabilities",[]):raise NSFWinfraCorePolicyError("CAPABILITY_NOT_REGISTERED")
 @staticmethod
 def classify_capability(capability:str)->str:
  return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(marker in capability.upper() for marker in SENSITIVE_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
 @staticmethod
 def age_and_content_policy()->dict[str,Any]:
  return {"adult_content_access":"AGE_VERIFICATION_AND_LAWFUL_POLICY_REQUIRED","min_age_policy":"18_PLUS_FOR_ADULT_CATEGORIES","default_adult_access":"DENY","consent_and_rights":"REQUIRED_WHERE_APPLICABLE","moderation":"PRODUCT_AND_APPLICATION_LAYER_ENFORCEMENT_REQUIRED","execution_performed":False}
 @staticmethod
 def safe_summary(item:dict[str,Any])->dict[str,Any]:
  blocked={"token","access_token","refresh_token","client_secret","api_key","secret","signed_url"}
  return {k:v for k,v in item.items() if k.casefold() not in blocked}
