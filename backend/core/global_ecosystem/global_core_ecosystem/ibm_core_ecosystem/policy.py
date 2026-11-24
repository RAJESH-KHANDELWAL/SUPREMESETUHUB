"""IBM Core metadata and authorization guardrails; does not authorize IBM API calls."""
from __future__ import annotations
from typing import Any
SENSITIVE_MARKERS=("ADMIN","DELETE","WRITE","CREATE","UPDATE","BILLING","IAM","SECRET","KEY","ROTATE","DEPLOY","NETWORK","PAYMENT")
BLOCKED_SECRET_KEYS={"token","access_token","refresh_token","api_key","apikey","secret","secret_value","client_secret","iam_api_key","authorization","password"}
class IBMCorePolicyError(PermissionError): pass
class IBMCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None: raise IBMCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator=getattr(context,"validate",None)
        if not callable(validator): raise IBMCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()
    @staticmethod
    def validate_capability(product: dict[str,Any], capability: str) -> None:
        if not product.get("enabled",True): raise IBMCorePolicyError("PRODUCT_DISABLED")
        if capability not in set(product.get("capabilities",[])): raise IBMCorePolicyError("CAPABILITY_NOT_REGISTERED")
    @staticmethod
    def classify_capability(capability: str) -> str:
        upper=capability.upper()
        return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(x in upper for x in SENSITIVE_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
    @staticmethod
    def sanitize(value: Any) -> Any:
        if isinstance(value,dict):
            return {k:IBMCorePolicy.sanitize(v) for k,v in value.items() if str(k).casefold() not in BLOCKED_SECRET_KEYS}
        if isinstance(value,list): return [IBMCorePolicy.sanitize(x) for x in value]
        if isinstance(value,tuple): return [IBMCorePolicy.sanitize(x) for x in value]
        return value
