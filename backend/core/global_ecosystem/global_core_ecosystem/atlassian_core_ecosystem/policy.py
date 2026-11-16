"""Metadata policy helpers; not a substitute for API authorization."""
from __future__ import annotations
from typing import Any
from .contracts import TenantContext

SENSITIVE_MARKERS = ("ADMIN", "DELETE", "WRITE", "PUBLISH", "PROVISION", "ACCESS", "PERMISSION", "CHANGE")

class AtlassianCorePolicy:
    @staticmethod
    def safe_module_summary(module: dict[str, Any]) -> dict[str, Any]:
        return {key: module.get(key) for key in ("ecosystem_id", "name", "ecosystem_type", "parent_id", "capabilities", "domains", "status", "enabled", "api_catalog_ref", "connected", "live_connection_verified", "api_available") if key in module}

    @staticmethod
    def classify_capability(capability: str) -> str:
        token = capability.upper()
        return "ELEVATED_REQUIRES_EXPLICIT_AUTHORIZATION" if any(marker in token for marker in SENSITIVE_MARKERS) else "STANDARD_PROVIDER_PERMISSION_REQUIRED"

    @staticmethod
    def require_tenant_context(context: TenantContext | None) -> None:
        if context is None: raise ValueError("TENANT_CONTEXT_REQUIRED")
        context.validate()

    @staticmethod
    def validate_capability(module: dict[str, Any], capability: str) -> None:
        if capability not in module.get("capabilities", []): raise PermissionError("CAPABILITY_NOT_REGISTERED")
