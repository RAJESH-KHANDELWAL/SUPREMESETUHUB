"""Reusable read-only provider Core service."""
from .catalog import get_provider
from .contracts import CoreResult,Readiness
from .policy import HostingCorePolicy
class HostingProviderCoreService:
 def __init__(self,provider_id):
  self.provider=get_provider(provider_id)
  if self.provider is None:raise LookupError(f"HOSTING_PROVIDER_NOT_REGISTERED: {provider_id}")
 def status(self):return {"success":True,**HostingCorePolicy.safe_summary(self.provider),"core_layer":"HOSTING_CORE","readiness":Readiness.CATALOG_ONLY.value,"live_connection_verified":False,"api_transport_in_core":False}
 def capabilities(self):
  caps=self.provider.get("capabilities",[]);return {"success":True,"provider_id":self.provider["provider_id"],"count":len(caps),"capabilities":[{"name":x,"authorization_class":HostingCorePolicy.classify_capability(x)} for x in caps]}
 def authorize_capability(self,capability,context):
  try:HostingCorePolicy.require_tenant_context(context);HostingCorePolicy.validate_capability(self.provider,capability)
  except (ValueError,PermissionError) as exc:return CoreResult(False,self.provider["ecosystem_id"],"POLICY_DENIED",errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
  return CoreResult(True,self.provider["ecosystem_id"],"METADATA_POLICY_PASSED",data={"capability":capability,"note":"Not provider authorization or API entitlement."},request_id=context.request_id).to_dict()
