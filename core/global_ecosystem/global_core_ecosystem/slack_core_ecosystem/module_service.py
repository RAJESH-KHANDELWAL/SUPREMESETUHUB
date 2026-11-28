"""Shared read-only service for Slack product Core packages."""
from typing import Any
from .contracts import CoreResult,TenantContext
from .policy import SlackCorePolicy
from .product_catalog import get_product
class SlackProductCoreService:
 PRODUCT_ID=""
 def __init__(self):
  if not self.PRODUCT_ID:raise NotImplementedError("PRODUCT_ID_REQUIRED")
  self._product=get_product(self.PRODUCT_ID)
  if self._product is None:raise LookupError("SLACK_PRODUCT_NOT_REGISTERED: "+self.PRODUCT_ID)
 def status(self):return {"success":True,**SlackCorePolicy.safe_metadata(self._product),"core_layer":"SLACK_CORE","live_connection_verified":False,"api_calls_performed":0}
 def capabilities(self):
  caps=self._product["capabilities"]
  return {"success":True,"ecosystem_id":self._product["ecosystem_id"],"count":len(caps),"capabilities":[{"name":c,"authorization_class":SlackCorePolicy.classify_capability(c)} for c in caps]}
 def authorize_capability(self,capability,context:TenantContext|None):
  try:SlackCorePolicy.require_tenant_context(context);SlackCorePolicy.validate_capability(self._product,capability)
  except (ValueError,PermissionError) as exc:return CoreResult(False,self._product["ecosystem_id"],"POLICY_DENIED",errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
  return CoreResult(True,self._product["ecosystem_id"],"CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED",data={"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,"authorization_class":SlackCorePolicy.classify_capability(capability),"api_call_performed":False},request_id=context.request_id).to_dict()
