"""Metadata policy boundary; provider auth and resource operations belong to API/Engine."""
from __future__ import annotations
from typing import Any
from .contracts import HostingTenantContext

SECRET_KEY_MARKERS = ("token", "secret", "password", "authorization", "api_key",
                      "private_key", "credential", "access_key", "secret_key")

class HostingCorePolicyError(PermissionError):
    pass

class HostingCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if not isinstance(context, HostingTenantContext):
            raise HostingCorePolicyError("AUTHENTICATED_HOSTING_TENANT_CONTEXT_REQUIRED")
        try:
            context.validate()
        except ValueError as exc:
            raise HostingCorePolicyError(str(exc)) from exc

    @staticmethod
    def validate_capability(provider: dict[str, Any], capability: str) -> None:
        if not provider.get("enabled", True):
            raise HostingCorePolicyError("PROVIDER_DISABLED")
        if capability not in set(provider.get("capabilities", [])):
            raise HostingCorePolicyError("CAPABILITY_NOT_REGISTERED")

    @staticmethod
    def sanitize(value: Any) -> Any:
        if isinstance(value, dict):
            return {key: HostingCorePolicy.sanitize(item) for key, item in value.items()
                    if not any(marker in str(key).casefold() for marker in SECRET_KEY_MARKERS)}
        if isinstance(value, list):
            return [HostingCorePolicy.sanitize(item) for item in value]
        if isinstance(value, tuple):
            return [HostingCorePolicy.sanitize(item) for item in value]
        return value

    @staticmethod
    def safe_provider_summary(provider: dict[str, Any]) -> dict[str, Any]:
        return HostingCorePolicy.sanitize(provider)
