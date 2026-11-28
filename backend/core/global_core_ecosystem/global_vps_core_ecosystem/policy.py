"""VPS Core authorization and metadata policy boundaries."""
from typing import Any
SENSITIVE_OPERATIONS={"create","start","stop","restart","resize","rebuild","delete","attach","detach","firewall_update","key_rotate","snapshot_restore"}
class VPSCorePolicyError(PermissionError): pass
def require_tenant_context(context:Any)->None:
 if context is None or not callable(getattr(context,"validate",None)): raise VPSCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
 context.validate()
def classify_operation(operation:str|None)->str:
 if not operation:return "READ_ONLY_METADATA"
 return "EXPLICIT_AUTHORIZATION_AND_AUDIT_REQUIRED" if operation.casefold() in SENSITIVE_OPERATIONS else "TENANT_AUTHORIZATION_REQUIRED"
def safe_provider_summary(provider:dict[str,Any])->dict[str,Any]:
 blocked={"token","access_token","refresh_token","api_key","client_secret","password","secret","private_key"}
 return {k:v for k,v in provider.items() if k.casefold() not in blocked}
