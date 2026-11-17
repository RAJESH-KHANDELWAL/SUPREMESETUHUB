"""Security CORE policy metadata; not a substitute for enforcement."""
from __future__ import annotations
from collections.abc import Mapping
from copy import deepcopy
SENSITIVE_KEYS=frozenset({"api_key","access_token","refresh_token","client_secret","token","secret","password","private_key","authorization","email","phone","mobile","address","government_id","passport_number","aadhaar_number","pan_number"})
HIGH_RISK=("ADMIN","DELETE","WRITE","PUBLISH","KEY_EXPORT","POLICY_CHANGE","ROLE_GRANT","CREDENTIAL")
class SecurityPolicyError(PermissionError): pass
def redact_sensitive_metadata(value):
    if isinstance(value,Mapping):
        return {str(k):redact_sensitive_metadata(v) for k,v in value.items() if str(k).casefold() not in SENSITIVE_KEYS}
    if isinstance(value,list): return [redact_sensitive_metadata(v) for v in value]
    if isinstance(value,tuple): return tuple(redact_sensitive_metadata(v) for v in value)
    return deepcopy(value)
def require_tenant_context(context):
    if context is None or not callable(getattr(context,"validate",None)): raise SecurityPolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
    try: context.validate()
    except (TypeError,ValueError) as exc: raise SecurityPolicyError(str(exc)) from exc
def classify_capability(capability):
    return "HIGH_RISK_REQUIRES_EXPLICIT_EXTERNAL_AUTHORIZATION" if any(x in capability.upper() for x in HIGH_RISK) else "TENANT_AUTHORIZATION_REQUIRED"
def validate_capability(provider,capability):
    if not provider.get("enabled",True): raise SecurityPolicyError("PROVIDER_DISABLED")
    if capability not in set(provider.get("capabilities",[])): raise SecurityPolicyError("CAPABILITY_NOT_REGISTERED")
def safe_provider_summary(provider): return redact_sensitive_metadata(provider)
def security_baseline():
    return {"least_privilege":True,"tenant_isolation_required":True,"mfa_recommended":True,"zero_trust_principle":True,"secrets_in_core":False,"auditability_required":True,"independent_runtime_enforcement_required":True}
