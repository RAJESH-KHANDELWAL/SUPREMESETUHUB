"""System Core metadata policy; never performs host authorization itself."""
from __future__ import annotations

from typing import Any

SENSITIVE_CAPABILITY_MARKERS = (
    "INSTALL", "UNINSTALL", "EXECUTE", "SHELL", "ROOT", "ADMIN",
    "KERNEL", "FIRMWARE", "DRIVER", "DELETE", "FORMAT", "ENCRYPT",
    "BOOT", "PATCH", "UPDATE", "REBOOT", "SHUTDOWN",
)


class SystemCorePolicyError(PermissionError):
    pass


class SystemCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None or not callable(getattr(context, "validate", None)):
            raise SystemCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        context.validate()

    @staticmethod
    def classify_capability(capability: str) -> str:
        upper = capability.upper()
        return (
            "HIGH_IMPACT_REQUIRES_EXPLICIT_AUTHORIZATION"
            if any(marker in upper for marker in SENSITIVE_CAPABILITY_MARKERS)
            else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
        )

    @staticmethod
    def safe_summary(record: dict[str, Any]) -> dict[str, Any]:
        blocked = {"token", "access_token", "refresh_token", "password", "secret", "private_key"}
        return {key: value for key, value in record.items() if key.casefold() not in blocked}
