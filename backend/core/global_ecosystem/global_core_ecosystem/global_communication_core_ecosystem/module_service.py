"""Shared read-only service for registered communication provider references."""
from __future__ import annotations
from typing import Any
from .catalog import get_communication_core_catalog
from .contracts import CoreResult, Readiness, TenantContext
from .policy import CommunicationCorePolicy

class CommunicationProviderCoreService:
    """Expose provider metadata and policy decisions, not live communication."""
    def __init__(self, provider_id: str) -> None:
        self.provider_id = provider_id.strip().casefold()
        self._module = next((p for p in get_communication_core_catalog()["providers"]
                             if p["id"].casefold() == self.provider_id), None)
        if self._module is None:
            raise LookupError(f"COMMUNICATION_PROVIDER_NOT_REGISTERED: {self.provider_id}")

    def status(self) -> dict[str, Any]:
        return {**CommunicationCorePolicy.safe_summary(self._module),
                "success": True, "core_layer": "GLOBAL_COMMUNICATION_CORE",
                "readiness": Readiness.CATALOG_ONLY.value,
                "api_transport_in_core": False, "live_connection_verified": False}

    def capabilities(self) -> dict[str, Any]:
        caps = self._module.get("capabilities", [])
        return {"success": True, "provider_id": self.provider_id, "count": len(caps),
                "capabilities": [{"name": item, "authorization_class":
                    "SENSITIVE" if item in {"SEND_MESSAGE", "SEND_EMAIL", "PLACE_CALL"} else "METADATA"}
                    for item in caps]}

    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str, Any]:
        try:
            CommunicationCorePolicy.require_tenant_context(context)
            CommunicationCorePolicy.require_explicit_authorization(capability, False)
        except (ValueError, PermissionError) as exc:
            return CoreResult(False, self._module["ecosystem_id"], "POLICY_DENIED",
                              errors=[str(exc)], request_id=getattr(context, "request_id", None)).to_dict()
        return CoreResult(True, self._module["ecosystem_id"],
                          "CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED",
                          data={"capability": capability, "api_call_performed": False},
                          request_id=context.request_id).to_dict()

__all__ = ["CommunicationProviderCoreService"]
