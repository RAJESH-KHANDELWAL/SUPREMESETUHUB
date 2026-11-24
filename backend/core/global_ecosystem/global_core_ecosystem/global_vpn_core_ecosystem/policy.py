"""VPN privacy, authorization and operation policy boundaries."""
from typing import Any
SENSITIVE_OPERATIONS={"connect","disconnect","reconnect","create_tunnel","delete_tunnel","change_route","change_dns","enable_kill_switch","disable_kill_switch","add_peer","remove_peer","rotate_key","change_exit_node"}
class VPNCorePolicyError(PermissionError):pass
def require_tenant_context(context:Any)->None:
 if context is None or not callable(getattr(context,"validate",None)):raise VPNCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
 context.validate()
def classify_operation(operation:str|None)->str:
 if not operation:return "READ_ONLY_METADATA"
 return "EXPLICIT_USER_CONSENT_AUTHORIZATION_AND_AUDIT_REQUIRED" if operation.casefold() in SENSITIVE_OPERATIONS else "TENANT_AUTHORIZATION_REQUIRED"
def safe_provider_summary(provider:dict[str,Any])->dict[str,Any]:
 blocked={"token","access_token","refresh_token","api_key","client_secret","password","secret","private_key","privatekey","psk","pre_shared_key"}
 return {k:v for k,v in provider.items() if k.casefold() not in blocked}
