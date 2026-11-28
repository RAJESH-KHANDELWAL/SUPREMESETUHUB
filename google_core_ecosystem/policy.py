"""Google Core policy guardrails.

This module deliberately does not authorize Google API operations by itself.
It validates Core metadata and caller context before a separately authorized
API-layer adapter is selected by the application.
"""
from __future__ import annotations

from typing import Any

SENSITIVE_CAPABILITY_MARKERS = (
    "ADMIN", "DELETE", "WRITE", "SEND", "UPLOAD", "PUBLISH",
    "BILLING", "IAM", "PERMISSION", "USER_GROUP",
)


class GoogleCorePolicyError(PermissionError):
    """Raised when a Core request violates a policy boundary."""


class GoogleCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None:
            raise GoogleCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator = getattr(context, "validate", None)
        if not callable(validator):
            raise GoogleCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()

    @staticmethod
    def validate_capability(module: dict[str, Any], capability: str) -> None:
        if not module.get("enabled", True):
            raise GoogleCorePolicyError("MODULE_DISABLED")
        allowed = set(module.get("capabilities", []))
        if capability not in allowed:
            raise GoogleCorePolicyError("CAPABILITY_NOT_REGISTERED")
        # A registered capability is descriptive metadata, not proof that
        # the caller has a Google OAuth grant or an API entitlement.

    @staticmethod
    def classify_capability(capability: str) -> str:
        upper = capability.upper()
        return (
            "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION"
            if any(marker in upper for marker in SENSITIVE_CAPABILITY_MARKERS)
            else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
        )

    @staticmethod
    def safe_module_summary(module: dict[str, Any]) -> dict[str, Any]:
        """Return public metadata only; strip credentials and token-like fields."""
        blocked = {"token", "access_token", "refresh_token", "client_secret", "api_key", "secret"}
        return {
            key: value for key, value in module.items()
            if key.casefold() not in blocked
        }
