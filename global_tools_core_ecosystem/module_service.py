"""Shared read-only provider service; no network or credential operations."""
from .catalog import get_provider
from .contracts import CoreResult
from .policy import ToolsCorePolicy
class ToolProviderCoreService:
 PROVIDER_ID=""
 def __init__(self):
  if not self.PROVIDER_ID: raise NotImplementedError("PROVIDER_ID_REQUIRED")
  self.provider=get_provider(self.PROVIDER_ID)
  if self.provider is None: raise LookupError("TOOLS_PROVIDER_NOT_REGISTERED")
 def status(self): return {"success":True,**ToolsCorePolicy.safe_summary(self.provider),"api_transport_in_core":False,"live_connection_verified":False}
 def authorize_capability(self,capability,context):
  try: ToolsCorePolicy.require_tenant(context); ToolsCorePolicy.validate_capability(self.provider,capability)
  except (ValueError,PermissionError) as e: return CoreResult(False,self.provider["ecosystem_id"],"POLICY_DENIED",errors=[str(e)]).to_dict()
  return CoreResult(True,self.provider["ecosystem_id"],"CORE_POLICY_PASSED_PROVIDER_AUTH_STILL_REQUIRED",data={"capability":capability,"tenant_id":context.tenant_id,"api_call_performed":False}).to_dict()
