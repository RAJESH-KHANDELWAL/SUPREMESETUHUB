"""OpenAI Core metadata policy and security boundaries."""
from __future__ import annotations

from typing import Any

SENSITIVE_CAPABILITY_MARKERS = (
    "ADMIN", "DELETE", "WRITE", "SEND", "PUBLISH", "BILLING",
    "KEY", "SECRET", "TOKEN", "USER", "ORGANIZATION", "WEBHOOK",
)


class OpenAICorePolicyError(PermissionError):
    """Raised when a Core metadata or tenant-context policy is violated."""


class OpenAICorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None:
            raise OpenAICorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator = getattr(context, "validate", None)
        if not callable(validator):
            raise OpenAICorePolicyError("INVALID_TENANT_CONTEXT")
        validator()

    @staticmethod
    def validate_capability(product: dict[str, Any], capability: str) -> None:
        if not product.get("enabled", True):
            raise OpenAICorePolicyError("PRODUCT_DISABLED")
        if product.get("status") == "retired_reference_only":
            raise OpenAICorePolicyError("RETIRED_PRODUCT_NOT_AVAILABLE")
        if capability not in set(product.get("capabilities", [])):
            raise OpenAICorePolicyError("CAPABILITY_NOT_REGISTERED")
        # Passing Core metadata policy is not OpenAI API authorization.

    @staticmethod
    def classify_capability(capability: str) -> str:
        upper = str(capability).upper()
        if any(marker in upper for marker in SENSITIVE_CAPABILITY_MARKERS):
            return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION"
        return "STANDARD_REQUIRES_TENANT_AUTHORIZATION"

    @staticmethod
    def safe_summary(value: dict[str, Any]) -> dict[str, Any]:
        """Recursively remove secret-like values from public metadata."""
        blocked = {
            "token", "access_token", "refresh_token", "client_secret",
            "api_key", "secret", "authorization", "password",
        }

        def clean(item: Any) -> Any:
            if isinstance(item, dict):
                return {
                    key: clean(val) for key, val in item.items()
                    if str(key).casefold() not in blocked
                }
            if isinstance(item, list):
                return [clean(value) for value in item]
            if isinstance(item, tuple):
                return [clean(value) for value in item]
            return item

        return clean(value)


__all__ = ["OpenAICorePolicy", "OpenAICorePolicyError"]
