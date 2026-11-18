"""Metadata policy checks for Global Storage Core; not provider IAM."""
from __future__ import annotations
from typing import Any

class StorageCorePolicyError(PermissionError):
    pass

class StorageCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None: raise StorageCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator = getattr(context, "validate", None)
        if not callable(validator): raise StorageCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()

    @staticmethod
    def validate_provider(provider: dict[str, Any]) -> None:
        if not provider.get("enabled", True): raise StorageCorePolicyError("STORAGE_PROVIDER_DISABLED")

    @staticmethod
    def validate_capability(provider: dict[str, Any], capability: str) -> None:
        StorageCorePolicy.validate_provider(provider)
        if capability not in set(provider.get("capabilities", [])): raise StorageCorePolicyError("STORAGE_CAPABILITY_NOT_REGISTERED")

    @staticmethod
    def safe_provider_summary(provider: dict[str, Any]) -> dict[str, Any]:
        blocked = {"token","access_token","refresh_token","client_secret","api_key","secret","credentials"}
        return {key:value for key,value in provider.items() if key.casefold() not in blocked}
