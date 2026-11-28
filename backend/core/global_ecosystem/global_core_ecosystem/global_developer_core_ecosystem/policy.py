"""Developer Core policy boundaries; never grants provider API access."""
from __future__ import annotations
from typing import Any

SENSITIVE_MARKERS=("WRITE","DELETE","ADMIN","PUBLISH","DEPLOY","BILLING","PAYMENT","SECRET","TOKEN","KEY","INVITE","GRANT","UPLOAD")
class DeveloperCorePolicyError(PermissionError): pass

class DeveloperCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None: raise DeveloperCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator=getattr(context,"validate",None)
        if not callable(validator): raise DeveloperCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()
    @staticmethod
    def validate_capability(module: dict[str,Any], capability: str) -> None:
        if not module.get("enabled",True): raise DeveloperCorePolicyError("MODULE_DISABLED")
        if capability not in module.get("capabilities",[]): raise DeveloperCorePolicyError("CAPABILITY_NOT_REGISTERED")
    @staticmethod
    def classify_capability(capability: str) -> str:
        upper=capability.upper()
        return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(x in upper for x in SENSITIVE_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
    @staticmethod
    def require_explicit_authorization(capability: str, authorized: bool) -> None:
        if any(x in capability.upper() for x in SENSITIVE_MARKERS) and not authorized:
            raise DeveloperCorePolicyError("EXPLICIT_AUTHORIZATION_REQUIRED")
    @staticmethod
    def safe_module_summary(module: dict[str,Any]) -> dict[str,Any]:
        blocked={"token","access_token","refresh_token","client_secret","api_key","secret","private_key"}
        return {k:v for k,v in module.items() if k.casefold() not in blocked}
