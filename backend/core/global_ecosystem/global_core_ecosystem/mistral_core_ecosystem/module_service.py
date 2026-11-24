"""Shared read-only service used by each Mistral product Core package."""
from __future__ import annotations
from typing import Any
from .catalog import get_mistral_core_catalog
from .contracts import CoreResult,TenantContext
from .policy import MistralCorePolicy

class MistralProductCoreService:
 def __init__(self,product_key:str)->None:
  key=product_key.strip().casefold()
  if not key: raise ValueError("PRODUCT_KEY_REQUIRED")
  self.product=next((p for p in get_mistral_core_catalog()["children"] if p["key"]==key),None)
  if self.product is None: raise LookupError(f"MISTRAL_PRODUCT_NOT_REGISTERED: {key}")
 def status(self)->dict[str,Any]:
  return {"success":True,"provider":"mistral",**MistralCorePolicy.safe_product_summary(self.product),
   "core_layer":"CORE","api_transport_in_core":False,"execution_in_core":False,
   "live_connection_verified":False,"api_calls_performed":0}
 def capabilities(self)->dict[str,Any]:
  rows=self.product["capabilities"]
  return {"success":True,"provider":"mistral","product":self.product["key"],"count":len(rows),
   "capabilities":[{"name":x,"authorization_class":MistralCorePolicy.classify_capability(x)} for x in rows]}
 def authorize_capability(self,capability:str,context:TenantContext)->dict[str,Any]:
  try:
   MistralCorePolicy.require_tenant_context(context)
   MistralCorePolicy.validate_capability(self.product,capability)
  except (ValueError,PermissionError) as exc:
   return CoreResult(False,self.product["ecosystem_id"],"POLICY_DENIED",
    errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
  return CoreResult(True,self.product["ecosystem_id"],"CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED",
   data={"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,
    "api_call_performed":False},request_id=context.request_id).to_dict()

__all__=["MistralProductCoreService"]
