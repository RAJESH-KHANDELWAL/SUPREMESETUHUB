"""Reusable read-only Atlassian product-family Core service."""
from __future__ import annotations
from typing import Any
from .catalog import get_atlassian_core_catalog
from .contracts import CoreResult, Readiness, TenantContext
from .policy import AtlassianCorePolicy

class AtlassianProductCoreService:
    ECOSYSTEM_ID = ""
    def __init__(self) -> None:
        if not self.ECOSYSTEM_ID: raise NotImplementedError("Product service must define ECOSYSTEM_ID")
        self._module = next((item for item in get_atlassian_core_catalog()["children"] if item["ecosystem_id"] == self.ECOSYSTEM_ID), None)
        if self._module is None: raise LookupError(f"ATLASSIAN_CORE_MODULE_NOT_REGISTERED: {self.ECOSYSTEM_ID}")

    def status(self) -> dict[str, Any]:
        return {**AtlassianCorePolicy.safe_module_summary(self._module), "success": True, "provider": "atlassian", "core_layer": "ATLASSIAN_CORE", "readiness": Readiness.CATALOG_ONLY.value, "api_transport_in_core": False, "live_connection_verified": False}

    def capabilities(self) -> dict[str, Any]:
        caps = self._module.get("capabilities", [])
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID, "count": len(caps), "capabilities": [{"name": cap, "authorization_class": AtlassianCorePolicy.classify_capability(cap)} for cap in caps]}

    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str, Any]:
        try:
            AtlassianCorePolicy.require_tenant_context(context)
            AtlassianCorePolicy.validate_capability(self._module, capability)
        except (ValueError, PermissionError) as exc:
            return CoreResult(False, self.ECOSYSTEM_ID, "POLICY_DENIED", errors=[str(exc)], request_id=getattr(context, "request_id", None)).to_dict()
        return CoreResult(True, self.ECOSYSTEM_ID, "CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED", data={"capability": capability, "tenant_id": context.tenant_id, "actor_id": context.actor_id, "api_call_performed": False}, request_id=context.request_id).to_dict()
