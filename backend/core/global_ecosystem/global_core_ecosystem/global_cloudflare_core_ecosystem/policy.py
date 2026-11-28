"""Cloudflare Core metadata and security policy boundaries."""
from __future__ import annotations
from typing import Any

class CloudflarePolicyError(PermissionError):
    """Raised when a request crosses the Cloudflare Core policy boundary."""

class CloudflareCorePolicy:
    SENSITIVE_MARKERS = ("DELETE", "WRITE", "PURGE", "BILLING", "TOKEN",
                         "KEY", "ADMIN", "ZONE_EDIT", "DNS_EDIT", "ACCESS_POLICY")
    @staticmethod
    def safe_product_summary(product: dict[str, Any]) -> dict[str, Any]:
        blocked = {"token", "api_token", "access_token", "secret", "api_key",
                   "client_secret", "private_key", "password"}
        return {k: v for k, v in product.items() if k.casefold() not in blocked}
    @classmethod
    def classify_capability(cls, capability: str) -> str:
        value = capability.upper()
        if any(marker in value for marker in cls.SENSITIVE_MARKERS):
            return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION"
        return "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None or not callable(getattr(context, "validate", None)):
            raise CloudflarePolicyError("VALIDATED_TENANT_CONTEXT_REQUIRED")
        context.validate()
