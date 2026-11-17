"""Shared read-only Core service for registered security providers."""
from __future__ import annotations

from typing import Any

from .constants import ECOSYSTEM_ID
from .contracts import CoreResult, Readiness, TenantContext
from .policy import (
    SecurityPolicyError,
    classify_capability,
    require_tenant_context,
    safe_provider_summary,
    validate_capability,
)
from .provider_catalog import get_provider


class SecurityProviderCoreService:
    """Expose provider identity and policy-aware capability metadata.

    This class performs no network I/O, provider authentication, scanning,
    detection, response execution or security-control enforcement.
    """

    def __init__(self, provider_id: str) -> None:
        provider = get_provider(provider_id)
        if provider is None:
            raise LookupError(f"SECURITY_PROVIDER_NOT_REGISTERED: {provider_id}")
        self._provider = provider

    def status(self) -> dict[str, Any]:
        """Return the safe provider summary and descriptive readiness."""
        return {
            "success": True,
            **safe_provider_summary(self._provider),
            "core_layer": "GLOBAL_SECURITY_CORE",
            "api_transport_in_core": False,
            "live_connection_verified": False,
            "readiness": self._readiness(),
        }

    def describe(self) -> dict[str, Any]:
        """Backward-compatible alias for status()."""
        return self.status()

    def _readiness(self) -> str:
        if not self._provider.get("enabled", True):
            return Readiness.DISABLED.value
        return Readiness.CATALOG_ONLY.value

    def readiness(self) -> dict[str, Any]:
        """Return readiness metadata without claiming a live integration."""
        return {
            "provider_id": self._provider["provider_id"],
            "status": self._readiness(),
            "catalog_ready": True,
            "configuration_required": True,
            "live_connection": False,
            "api_calls_performed": 0,
            "security_enforcement_verified": False,
        }

    def capabilities(self) -> dict[str, Any]:
        capabilities = self._provider.get("capabilities", [])
        return {
            "success": True,
            "provider_id": self._provider["provider_id"],
            "count": len(capabilities),
            "capabilities": [
                {
                    "name": item,
                    "authorization_class": classify_capability(item),
                }
                for item in capabilities
            ],
        }

    def authorize_capability(
        self,
        capability: str,
        context: TenantContext | None,
    ) -> dict[str, Any]:
        """Validate Core metadata and context; external authorization is still required."""
        try:
            require_tenant_context(context)
            validate_capability(self._provider, capability)
        except (ValueError, PermissionError, SecurityPolicyError) as exc:
            return CoreResult(
                success=False,
                ecosystem_id=self._provider["ecosystem_id"],
                status="POLICY_DENIED",
                errors=[str(exc)],
                request_id=getattr(context, "request_id", None),
            ).to_dict()

        return CoreResult(
            success=True,
            ecosystem_id=self._provider["ecosystem_id"],
            status="CORE_POLICY_PASSED_EXTERNAL_AUTHORIZATION_REQUIRED",
            data={
                "capability": capability,
                "tenant_id": context.tenant_id,
                "actor_id": context.actor_id,
                "authorization_class": classify_capability(capability),
                "provider_call_performed": False,
                "security_control_executed": False,
            },
            request_id=context.request_id,
        ).to_dict()


__all__ = ["SecurityProviderCoreService", "ECOSYSTEM_ID"]
