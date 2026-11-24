"""Microsoft Core metadata policy; never a substitute for OAuth or API authorization."""
from __future__ import annotations
from typing import Any

SENSITIVE_MARKERS = ("ADMIN", "DELETE", "WRITE", "SEND", "UPLOAD", "PUBLISH", "BILLING", "ROLE", "PERMISSION", "USER", "SECRET", "TOKEN")

class MicrosoftCorePolicyError(PermissionError):
    """Raised when a Core metadata request violates a declared policy boundary."""

class MicrosoftCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None:
            raise MicrosoftCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator = getattr(context, "validate", None)
        if not callable(validator):
            raise MicrosoftCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()

    @staticmethod
    def validate_capability(module: dict[str, Any], capability: str) -> None:
        if not module.get("enabled", True):
            raise MicrosoftCorePolicyError("MODULE_DISABLED")
        if capability not in set(module.get("capabilities", [])):
            raise MicrosoftCorePolicyError("CAPABILITY_NOT_REGISTERED")

    @staticmethod
    def classify_capability(capability: str) -> str:
        upper = capability.upper()
        return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(x in upper for x in SENSITIVE_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"

    @staticmethod
    def safe_module_summary(module: dict[str, Any]) -> dict[str, Any]:
        blocked = {"token", "access_token", "refresh_token", "client_secret", "api_key", "secret", "password", "credential"}
        return {key: value for key, value in module.items() if key.casefold() not in blocked}
