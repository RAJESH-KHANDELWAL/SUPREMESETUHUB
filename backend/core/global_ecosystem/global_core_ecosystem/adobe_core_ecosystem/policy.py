"""Adobe Core metadata policy guardrails; not provider API authorization."""
from __future__ import annotations
from typing import Any
SENSITIVE_CAPABILITY_MARKERS=("ADMIN","DELETE","WRITE","SEND","UPLOAD","PUBLISH","BILLING","PERMISSION","USER","SIGN","COMMERCE","LICENSE")
class AdobeCorePolicyError(PermissionError):
    """Raised when a Core request violates a metadata policy boundary."""
class AdobeCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None: raise AdobeCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator=getattr(context,"validate",None)
        if not callable(validator): raise AdobeCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()
    @staticmethod
    def validate_capability(module: dict[str,Any], capability: str) -> None:
        if not module.get("enabled",True): raise AdobeCorePolicyError("MODULE_DISABLED")
        if capability not in set(module.get("capabilities",[])):
            raise AdobeCorePolicyError("CAPABILITY_NOT_REGISTERED")
    @staticmethod
    def classify_capability(capability: str) -> str:
        value=capability.upper()
        return ("SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION"
                if any(marker in value for marker in SENSITIVE_CAPABILITY_MARKERS)
                else "STANDARD_REQUIRES_TENANT_AUTHORIZATION")
    @staticmethod
    def safe_module_summary(module: dict[str,Any]) -> dict[str,Any]:
        blocked={"token","access_token","refresh_token","client_secret","api_key","secret","authorization","password"}
        return {key:value for key,value in module.items() if key.casefold() not in blocked}
