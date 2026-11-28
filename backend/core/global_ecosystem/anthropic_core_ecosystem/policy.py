"""Anthropic Core metadata policy; not a substitute for API authorization."""
from __future__ import annotations
from typing import Any

SENSITIVE_MARKERS=("ADMIN","DELETE","UPLOAD","WRITE","WORKSPACE","CREDENTIAL","IDENTITY","MANAGED_AGENT")

class AnthropicCorePolicyError(PermissionError):
    pass

class AnthropicCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None: raise AnthropicCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator=getattr(context,"validate",None)
        if not callable(validator): raise AnthropicCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()

    @staticmethod
    def validate_capability(module: dict[str, Any], capability: str) -> None:
        if not module.get("enabled",True): raise AnthropicCorePolicyError("MODULE_DISABLED")
        if capability not in set(module.get("capabilities",[])):
            raise AnthropicCorePolicyError("CAPABILITY_NOT_REGISTERED")

    @staticmethod
    def classify_capability(capability: str) -> str:
        upper=capability.upper()
        return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(x in upper for x in SENSITIVE_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"

    @staticmethod
    def safe_module_summary(module: dict[str, Any]) -> dict[str, Any]:
        blocked={"token","access_token","refresh_token","api_key","client_secret","secret","credential_value"}
        return {k:v for k,v in module.items() if k.casefold() not in blocked}
