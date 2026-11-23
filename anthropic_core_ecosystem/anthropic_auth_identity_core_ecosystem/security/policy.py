"""Capability policy metadata; final authorization belongs to application/API layers."""
SENSITIVE=["ANTHROPIC_CREDENTIAL_READINESS","ANTHROPIC_WORKLOAD_IDENTITY_BOUNDARY","ANTHROPIC_CREDENTIAL_ROTATION_BOUNDARY"]

def evaluate(capability: str, *, tenant_authorized: bool = False, explicit_permission: bool = False) -> dict:
    if capability not in ["ANTHROPIC_CREDENTIAL_READINESS","ANTHROPIC_WORKLOAD_IDENTITY_BOUNDARY","ANTHROPIC_CREDENTIAL_ROTATION_BOUNDARY"]:
        return {"allowed":False,"reason":"CAPABILITY_NOT_REGISTERED"}
    if not tenant_authorized:
        return {"allowed":False,"reason":"TENANT_AUTHORIZATION_REQUIRED"}
    if capability in SENSITIVE and not explicit_permission:
        return {"allowed":False,"reason":"EXPLICIT_PERMISSION_REQUIRED"}
    return {"allowed":True,"reason":"CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED"}
