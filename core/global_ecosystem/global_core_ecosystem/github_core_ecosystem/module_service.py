"""Shared read-only Core service for GitHub API families."""
from .catalog import list_github_families
from .contracts import CoreResult
from .policy import GitHubCorePolicy
class GitHubProductCoreService:
 FAMILY=""
 def __init__(self):
  if not self.FAMILY: raise NotImplementedError("FAMILY_REQUIRED")
  self._module=next((x for x in list_github_families() if x["family"]==self.FAMILY),None)
  if self._module is None: raise LookupError("GITHUB_CORE_FAMILY_NOT_REGISTERED")
 def status(self): return {**GitHubCorePolicy.safe_summary(self._module),"core_layer":"GITHUB_CORE","api_transport_in_core":False,"live_connection_verified":False}
 def capabilities(self):
  values=self._module.get("capabilities",[])
  return {"success":True,"family":self.FAMILY,"count":len(values),"capabilities":[{"name":x,"authorization_class":GitHubCorePolicy.classify_capability(x)} for x in values]}
 def authorize_capability(self,capability,context):
  try: GitHubCorePolicy.require_tenant_context(context); GitHubCorePolicy.validate_capability(self._module,capability)
  except (ValueError,PermissionError) as exc: return CoreResult(False,self._module["ecosystem_id"],"POLICY_DENIED",errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
  return CoreResult(True,self._module["ecosystem_id"],"CORE_POLICY_PASSED_PROVIDER_AUTHORIZATION_STILL_REQUIRED",data={"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,"provider_api_call_performed":False},request_id=context.request_id).to_dict()
