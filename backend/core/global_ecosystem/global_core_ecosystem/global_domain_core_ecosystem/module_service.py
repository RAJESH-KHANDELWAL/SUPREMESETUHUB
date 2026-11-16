"""Shared read-only provider Core service for domain provider packages."""
from __future__ import annotations
from typing import Any
from .contracts import DomainCoreResult, DomainReadiness, DomainTenantContext
from .policy import DomainCorePolicy
from .provider_catalog import get_domain_provider

class DomainProviderCoreService:
    PROVIDER_ID = ""

    def __init__(self) -> None:
        if not self.PROVIDER_ID:
            raise NotImplementedError("Provider service must define PROVIDER_ID")
        provider = get_domain_provider(self.PROVIDER_ID)
        if provider is None:
            raise LookupError(f"DOMAIN_PROVIDER_NOT_REGISTERED: {self.PROVIDER_ID}")
        self._provider = provider

    def status(self) -> dict[str, Any]:
        return {
            **DomainCorePolicy.safe_provider_summary(self._provider),
            "core_layer": "GLOBAL_DOMAIN_CORE",
            "api_transport_in_core": False,
            "live_connection_verified": False,
            "readiness": DomainReadiness.CATALOG_ONLY.value,
        }

    def capabilities(self) -> dict[str, Any]:
        items = self._provider.get("capabilities", [])
        return {"success": True, "provider_id": self.PROVIDER_ID, "count": len(items),
                "capabilities": [{"name": item, "authorization_class": "TENANT_AND_PROVIDER_AUTHORIZATION_REQUIRED"}
                                 for item in items]}

    def authorize_capability(self, capability: str, context: DomainTenantContext | None) -> dict[str, Any]:
        try:
            DomainCorePolicy.require_tenant_context(context)
            DomainCorePolicy.validate_capability(self._provider, capability)
        except (ValueError, PermissionError) as exc:
            return DomainCoreResult(False, self._provider["ecosystem_id"], "POLICY_DENIED",
                                     errors=[str(exc)], request_id=getattr(context, "request_id", None)).to_dict()
        return DomainCoreResult(
            True, self._provider["ecosystem_id"], "CORE_POLICY_PASSED_PROVIDER_AUTH_STILL_REQUIRED",
            data={"provider_id": self.PROVIDER_ID, "capability": capability,
                  "tenant_id": context.tenant_id, "actor_id": context.actor_id,
                  "provider_api_call_performed": False},
            request_id=context.request_id,
        ).to_dict()
