"""Reusable read-only Apple product-family Core service."""
from __future__ import annotations
from typing import Any
from .catalog import get_apple_core_catalog
from .contracts import CoreResult,Readiness,TenantContext
from .policy import AppleCorePolicy
class AppleProductCoreService:
 ECOSYSTEM_ID=""
 def __init__(self)->None:
  if not self.ECOSYSTEM_ID: raise NotImplementedError("Product service must define ECOSYSTEM_ID")
  self._module=self._find_module(self.ECOSYSTEM_ID)
 @staticmethod
 def _find_module(ecosystem_id:str)->dict[str,Any]:
  for item in get_apple_core_catalog()["children"]:
   if item["ecosystem_id"]==ecosystem_id:return item
  raise LookupError(f"APPLE_CORE_MODULE_NOT_REGISTERED: {ecosystem_id}")
 def status(self)->dict[str,Any]:
  return {**AppleCorePolicy.safe_module_summary(self._module),"success":True,"provider":"apple","core_layer":"APPLE_CORE","api_transport_in_core":False,"live_connection_verified":False,"readiness":Readiness.CATALOG_ONLY.value}
 def capabilities(self)->dict[str,Any]:
  caps=self._module.get("capabilities",[])
  return {"success":True,"ecosystem_id":self.ECOSYSTEM_ID,"count":len(caps),"capabilities":[{"name":c,"authorization_class":AppleCorePolicy.classify_capability(c)} for c in caps]}
 def authorize_capability(self,capability:str,context:TenantContext|None)->dict[str,Any]:
  try: AppleCorePolicy.require_tenant_context(context); AppleCorePolicy.validate_capability(self._module,capability)
  except (ValueError,PermissionError) as exc:return CoreResult(False,self.ECOSYSTEM_ID,"POLICY_DENIED",errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
  return CoreResult(True,self.ECOSYSTEM_ID,"CORE_POLICY_PASSED_APPLE_API_AUTH_STILL_REQUIRED",data={"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,"api_call_performed":False},request_id=context.request_id).to_dict()
