"""Shared read-only Core service for Anthropic product families."""
from __future__ import annotations
from typing import Any
from .catalog import list_anthropic_core_modules
from .contracts import CoreResult, Readiness, TenantContext
from .policy import AnthropicCorePolicy

class AnthropicProductCoreService:
    ECOSYSTEM_ID=""
    def __init__(self):
        if not self.ECOSYSTEM_ID: raise NotImplementedError("Product service must define ECOSYSTEM_ID")
        self._module=self._find_module(self.ECOSYSTEM_ID)

    @staticmethod
    def _find_module(ecosystem_id: str) -> dict[str,Any]:
        for item in list_anthropic_core_modules():
            if item["ecosystem_id"]==ecosystem_id: return item
        raise LookupError(f"ANTHROPIC_CORE_MODULE_NOT_REGISTERED: {ecosystem_id}")

    def status(self) -> dict[str,Any]:
        module=AnthropicCorePolicy.safe_module_summary(self._module)
        return { "success":True, **module, "core_layer":"ANTHROPIC_CORE",
                 "api_transport_in_core":False, "live_connection_verified":False,
                 "readiness":self._readiness() }

    def _readiness(self) -> str:
        if not self._module.get("enabled",True): return Readiness.DISABLED.value
        return Readiness.CATALOG_ONLY.value

    def capabilities(self) -> dict[str,Any]:
        items=self._module.get("capabilities",[])
        return {"success":True,"ecosystem_id":self.ECOSYSTEM_ID,"count":len(items),
                "capabilities":[{"name":x,"authorization_class":AnthropicCorePolicy.classify_capability(x)} for x in items]}

    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str,Any]:
        try:
            AnthropicCorePolicy.require_tenant_context(context)
            AnthropicCorePolicy.validate_capability(self._module,capability)
        except (ValueError,PermissionError) as exc:
            return CoreResult(False,self.ECOSYSTEM_ID,"POLICY_DENIED",errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
        return CoreResult(True,self.ECOSYSTEM_ID,"CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED",
            data={"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,
                  "authorization_class":AnthropicCorePolicy.classify_capability(capability),"api_call_performed":False},
            request_id=context.request_id).to_dict()
