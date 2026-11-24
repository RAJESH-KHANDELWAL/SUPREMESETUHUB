"""Reusable read-only service for a registered human-language provider."""
from __future__ import annotations

from typing import Any

from .contracts import CoreResult, Readiness, TenantContext
from .policy import (
    HumanLanguagePolicyError, classify_capability, require_tenant_context,
    safe_provider_summary, validate_capability,
)
from .provider_catalog import get_provider


class HumanLanguageProviderCoreService:
    """Provider identity and capability metadata; never performs network I/O."""

    def __init__(self, provider_id: str) -> None:
        provider = get_provider(provider_id)
        if provider is None:
            raise LookupError(f"HUMAN_LANGUAGE_PROVIDER_NOT_REGISTERED: {provider_id}")
        self._provider = provider
        self.ECOSYSTEM_ID = provider["ecosystem_id"]

    def describe(self) -> dict[str, Any]:
        return {
            "success": True,
            **safe_provider_summary(self._provider),
            "core_layer": "GLOBAL_HUMAN_LANGUAGE_CORE",
            "api_transport_in_core": False,
            "live_connection_verified": False,
        }

    def readiness(self) -> dict[str, Any]:
        return {
            "provider_id": self._provider["provider_id"],
            "status": Readiness.CATALOG_ONLY.value,
            "catalog_ready": True,
            "configuration_required": True,
            "live_connection": False,
            "api_calls_performed": 0,
        }

    def capabilities(self) -> dict[str, Any]:
        items = self._provider.get("capabilities", [])
        return {
            "success": True,
            "provider_id": self._provider["provider_id"],
            "count": len(items),
            "capabilities": [
                {"name": item, "authorization_class": classify_capability(item)}
                for item in items
            ],
        }

    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str, Any]:
        try:
            require_tenant_context(context)
            validate_capability(self._provider, capability)
        except (ValueError, PermissionError, HumanLanguagePolicyError) as exc:
            return CoreResult(
                success=False,
                ecosystem_id=self.ECOSYSTEM_ID,
                status="POLICY_DENIED",
                errors=[str(exc)],
                request_id=getattr(context, "request_id", None),
            ).to_dict()
        return CoreResult(
            success=True,
            ecosystem_id=self.ECOSYSTEM_ID,
            status="CORE_POLICY_PASSED_EXTERNAL_PROVIDER_AUTH_STILL_REQUIRED",
            data={
                "capability": capability,
                "tenant_id": context.tenant_id,
                "actor_id": context.actor_id,
                "authorization_class": classify_capability(capability),
                "provider_call_performed": False,
            },
            request_id=context.request_id,
        ).to_dict()
