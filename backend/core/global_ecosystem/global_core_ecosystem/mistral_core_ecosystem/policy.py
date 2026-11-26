"""Mistral Core policy boundaries; this module does not authorize API calls."""
from __future__ import annotations
from typing import Any

SENSITIVE_CAPABILITY_MARKERS=("DELETE","WRITE","UPLOAD","TRAIN","FINE_TUN","BILLING","ADMIN","TOOL","PUBLISH","EXPORT","DATASET")

class MistralCorePolicyError(PermissionError): pass

class MistralCorePolicy:
 @staticmethod
 def require_tenant_context(context:Any)->None:
  if context is None: raise MistralCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
  validator=getattr(context,"validate",None)
  if not callable(validator): raise MistralCorePolicyError("INVALID_TENANT_CONTEXT")
  validator()
 @staticmethod
 def validate_capability(product:dict[str,Any],capability:str)->None:
  if not product.get("enabled",True): raise MistralCorePolicyError("PRODUCT_DISABLED")
  if capability not in set(product.get("capabilities",[])): raise MistralCorePolicyError("CAPABILITY_NOT_REGISTERED")
 @staticmethod
 def classify_capability(capability:str)->str:
  upper=capability.upper()
  return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(x in upper for x in SENSITIVE_CAPABILITY_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
 @staticmethod
 def safe_product_summary(product:dict[str,Any])->dict[str,Any]:
  blocked={"token","access_token","refresh_token","api_key","client_secret","secret","password"}
  return {k:v for k,v in product.items() if k.casefold() not in blocked}

__all__=["MistralCorePolicy","MistralCorePolicyError","SENSITIVE_CAPABILITY_MARKERS"]
