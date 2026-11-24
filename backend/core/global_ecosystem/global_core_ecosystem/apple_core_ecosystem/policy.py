"""Apple Core metadata policy; this is not Apple API authorization."""
from __future__ import annotations
from typing import Any
SENSITIVE_MARKERS=("ADMIN","DELETE","WRITE","PAY","PAYMENT","PURCHASE","DEVICE_COMMAND","PUBLISH","REFUND")
class AppleCorePolicyError(PermissionError): pass
class AppleCorePolicy:
 @staticmethod
 def require_tenant_context(context:Any)->None:
  if context is None: raise AppleCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
  validator=getattr(context,"validate",None)
  if not callable(validator): raise AppleCorePolicyError("INVALID_TENANT_CONTEXT")
  validator()
 @staticmethod
 def validate_capability(module:dict[str,Any],capability:str)->None:
  if not module.get("enabled",True): raise AppleCorePolicyError("MODULE_DISABLED")
  if capability not in set(module.get("capabilities",[])): raise AppleCorePolicyError("CAPABILITY_NOT_REGISTERED")
 @staticmethod
 def classify_capability(capability:str)->str:
  return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(x in capability.upper() for x in SENSITIVE_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
 @staticmethod
 def safe_module_summary(module:dict[str,Any])->dict[str,Any]:
  blocked={"token","access_token","refresh_token","client_secret","api_key","secret","private_key","key_material"}
  return {k:v for k,v in module.items() if k.casefold() not in blocked}
