"""Metadata policy boundaries for Global Domain Core; not provider authorization."""
from __future__ import annotations
from typing import Any
from .contracts import DomainTenantContext

SECRET_KEY_MARKERS = (
    "token", "secret", "password", "authorization", "auth_code",
    "transfer_code", "api_key", "private_key", "credential",
)

class DomainCorePolicyError(PermissionError):
    pass

class DomainCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if not isinstance(context, DomainTenantContext):
            raise DomainCorePolicyError("AUTHENTICATED_DOMAIN_TENANT_CONTEXT_REQUIRED")
        try:
            context.validate()
        except ValueError as exc:
            raise DomainCorePolicyError(str(exc)) from exc

    @staticmethod
    def validate_capability(provider: dict[str, Any], capability: str) -> None:
        if not provider.get("enabled", True):
            raise DomainCorePolicyError("PROVIDER_DISABLED")
        if capability not in set(provider.get("capabilities", [])):
            raise DomainCorePolicyError("CAPABILITY_NOT_REGISTERED")
        # This is metadata validation only. Provider consent, entitlements and
        # authorization must be enforced by the API/application layers.

    @staticmethod
    def sanitize(value: Any) -> Any:
        if isinstance(value, dict):
            clean = {}
            for key, item in value.items():
                key_text = str(key).casefold()
                if any(marker in key_text for marker in SECRET_KEY_MARKERS):
                    continue
                clean[key] = DomainCorePolicy.sanitize(item)
            return clean
        if isinstance(value, list):
            return [DomainCorePolicy.sanitize(item) for item in value]
        if isinstance(value, tuple):
            return [DomainCorePolicy.sanitize(item) for item in value]
        return value

    @staticmethod
    def safe_provider_summary(provider: dict[str, Any]) -> dict[str, Any]:
        return DomainCorePolicy.sanitize(provider)
