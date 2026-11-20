"""DigitalOcean Core policy and metadata guardrails."""
from __future__ import annotations

from typing import Any

SENSITIVE_CAPABILITY_MARKERS = (
    "DELETE", "DESTROY", "WRITE", "UPLOAD", "BILLING",
    "ADMIN", "FIREWALL", "SSH_KEY", "TOKEN",
)
SECRET_KEYS = frozenset({
    "token", "access_token", "refresh_token", "client_secret",
    "api_key", "secret", "authorization", "password",
})


class DigitalOceanCorePolicyError(PermissionError):
    """Raised when a Core request violates a policy boundary."""


class DigitalOceanCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None:
            raise DigitalOceanCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator = getattr(context, "validate", None)
        if not callable(validator):
            raise DigitalOceanCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()

    @staticmethod
    def validate_capability(capability: str, *, enabled: bool = True) -> None:
        if not enabled:
            raise DigitalOceanCorePolicyError("CAPABILITY_DISABLED")
        if not isinstance(capability, str) or not capability.strip():
            raise DigitalOceanCorePolicyError("CAPABILITY_REQUIRED")

    @staticmethod
    def classify_capability(capability: str) -> str:
        upper = capability.upper()
        return (
            "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION"
            if any(marker in upper for marker in SENSITIVE_CAPABILITY_MARKERS)
            else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
        )

    @staticmethod
    def safe_metadata(value: dict[str, Any]) -> dict[str, Any]:
        return {
            key: item for key, item in value.items()
            if str(key).casefold() not in SECRET_KEYS
        }
