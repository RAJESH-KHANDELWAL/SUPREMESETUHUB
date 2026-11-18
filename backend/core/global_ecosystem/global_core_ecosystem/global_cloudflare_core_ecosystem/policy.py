"""Cloudflare Core policy checks; descriptive metadata is not API authorization."""
from __future__ import annotations

from typing import Any

from .contracts import CloudflareTenantContext


class CloudflareCorePolicyError(PermissionError):
    """Raised when Core metadata or caller context violates policy."""


class CloudflareCorePolicy:
    @staticmethod
    def require_tenant_context(context: CloudflareTenantContext | None) -> None:
        if context is None or not isinstance(context, CloudflareTenantContext):
            raise CloudflareCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        try:
            context.validate()
        except ValueError as exc:
            raise CloudflareCorePolicyError("INVALID_TENANT_CONTEXT") from exc

    @staticmethod
    def validate_capability(product: dict[str, Any], capability: str) -> None:
        if product.get("status") != "CORE_CATALOG_ONLY":
            raise CloudflareCorePolicyError("PRODUCT_NOT_REGISTERED")
        if capability not in set(product.get("capabilities", ())):
            raise CloudflareCorePolicyError("CAPABILITY_NOT_REGISTERED")
        # A catalog entry does not grant API token scopes, account permissions,
        # product entitlements or authorization to perform a provider operation.

    @staticmethod
    def safe_product_summary(product: dict[str, Any]) -> dict[str, Any]:
        allowed = {
            "id", "name", "category", "capabilities", "core_path",
            "ecosystem_id", "status", "live_connection",
        }
        return {key: value for key, value in product.items() if key in allowed}


__all__ = ["CloudflareCorePolicy", "CloudflareCorePolicyError"]
