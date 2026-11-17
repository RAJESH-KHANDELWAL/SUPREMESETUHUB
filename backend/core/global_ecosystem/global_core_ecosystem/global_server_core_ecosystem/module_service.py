"""Reusable read-only provider metadata service for Server Core."""
from __future__ import annotations
from typing import Any
from .contracts import CoreResult, Readiness, TenantContext
from .policy import ServerCorePolicy
from .provider_catalog import get_provider

class ServerProviderCoreService:
    """Expose provider metadata without SDK calls, credentials or remote execution."""
    PROVIDER_ID = ""

    def __init__(self) -> None:
        if not self.PROVIDER_ID:
            raise NotImplementedError("Provider service must define PROVIDER_ID")
        self._module = get_provider(self.PROVIDER_ID)
        if self._module is None:
            raise LookupError(f"SERVER_CORE_PROVIDER_NOT_REGISTERED: {self.PROVIDER_ID}")

    def status(self) -> dict[str, Any]:
        return {**ServerCorePolicy.safe_summary(self._module), "core_layer":"SERVER_CORE",
                "api_transport_in_core":False, "live_connection_verified":False,
                "readiness":Readiness.METADATA_AVAILABLE.value}

    def capabilities(self) -> dict[str, Any]:
        capabilities = self._module.get("capabilities", [])
        return {"success":True,"provider_id":self.PROVIDER_ID,"count":len(capabilities),
                "capabilities":[{"name":item,"authorization_class":ServerCorePolicy.classify_capability(item)} for item in capabilities]}

    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str, Any]:
        try:
            ServerCorePolicy.require_tenant_context(context)
            ServerCorePolicy.validate_capability(self._module, capability)
        except (ValueError, PermissionError) as exc:
            return CoreResult(False, self._module.get("provider_id", self.PROVIDER_ID),
                              "POLICY_DENIED", errors=[str(exc)],
                              request_id=getattr(context,"request_id",None)).to_dict()
        return CoreResult(True, self._module.get("provider_id", self.PROVIDER_ID),
                          "CORE_POLICY_PASSED_PROVIDER_AUTH_STILL_REQUIRED",
                          data={"capability":capability,"tenant_id":context.tenant_id,
                                "actor_id":context.actor_id,
                                "authorization_class":ServerCorePolicy.classify_capability(capability),
                                "api_call_performed":False},
                          request_id=context.request_id).to_dict()
