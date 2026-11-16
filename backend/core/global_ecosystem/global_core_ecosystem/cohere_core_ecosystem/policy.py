"""Cohere CORE metadata policy; not a substitute for provider authorization."""
from __future__ import annotations

from typing import Any

from .catalog import CAPABILITIES
from .policies import ensure_operation_allowed

SENSITIVE_CAPABILITY_MARKERS = ("DELETE", "WRITE", "ADMIN", "BILLING", "DEPLOY", "TRAIN")


class CohereCorePolicyError(PermissionError):
    """Raised when a Cohere CORE policy boundary is violated."""


class CohereCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None:
            raise CohereCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator = getattr(context, "validate", None)
        if not callable(validator):
            raise CohereCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()

    @staticmethod
    def validate_capability(capability: str) -> None:
        if not isinstance(capability, str) or capability.strip().lower() not in CAPABILITIES:
            raise CohereCorePolicyError("CAPABILITY_NOT_REGISTERED")

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
        blocked = {"token", "access_token", "refresh_token", "client_secret", "api_key", "secret", "password"}
        return {key: value for key, value in module.items() if key.casefold() not in blocked}


__all__ = ["CohereCorePolicy", "CohereCorePolicyError", "ensure_operation_allowed"]
