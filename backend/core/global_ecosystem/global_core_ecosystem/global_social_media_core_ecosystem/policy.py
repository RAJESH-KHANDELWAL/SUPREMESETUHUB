"""Policy metadata checks for Social Media Core; no provider authorization."""
from __future__ import annotations
from typing import Any
from .contracts import TenantContext
from .platform_catalog import get_platform

class SocialMediaCorePolicyError(PermissionError):
    """Raised when a Core metadata policy check fails."""

class SocialMediaCorePolicy:
    SECRET_KEYS = {"access_token", "refresh_token", "client_secret", "api_key", "password", "private_key", "secret"}

    @staticmethod
    def require_tenant_context(context: TenantContext | None) -> TenantContext:
        if context is None:
            raise ValueError("TENANT_CONTEXT_REQUIRED")
        context.validate()
        return context

    @staticmethod
    def validate_platform(platform_id: str) -> dict[str, Any]:
        return get_platform(platform_id)

    @staticmethod
    def classify_capability(capability: str) -> str:
        value = capability.upper()
        if any(term in value for term in ("DELETE", "ADMIN", "BILLING", "PUBLISH", "MESSAGE_SEND", "POST_CREATE")):
            return "RESTRICTED"
        if any(term in value for term in ("READ", "VIEW", "LIST", "PROFILE")):
            return "READ"
        return "METADATA"

    @classmethod
    def redact(cls, value: Any) -> Any:
        if isinstance(value, dict):
            return {key: ("[REDACTED]" if key.lower() in cls.SECRET_KEYS else cls.redact(item)) for key, item in value.items()}
        if isinstance(value, list):
            return [cls.redact(item) for item in value]
        if isinstance(value, tuple):
            return [cls.redact(item) for item in value]
        return value
