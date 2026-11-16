"""Shared read-only Core facade for Adobe product families."""
from __future__ import annotations
from typing import Any
from .catalog import get_adobe_core_catalog
from .contracts import CoreResult, Readiness, TenantContext
from .policy import AdobeCorePolicy

class AdobeProductCoreService:
    ECOSYSTEM_ID = ""
    def __init__(self) -> None:
        if not self.ECOSYSTEM_ID: raise NotImplementedError("Product service must define ECOSYSTEM_ID")
        self._module = self._find_module(self.ECOSYSTEM_ID)
    @staticmethod
    def _find_module(ecosystem_id: str) -> dict[str,Any]:
        for item in get_adobe_core_catalog()["children"]:
            if item["ecosystem_id"] == ecosystem_id: return item
        raise LookupError(f"ADOBE_CORE_MODULE_NOT_REGISTERED: {ecosystem_id}")
    def status(self) -> dict[str,Any]:
        return {"success":True, **AdobeCorePolicy.safe_module_summary(self._module),
                "core_layer":"ADOBE_CORE", "api_transport_in_core":False,
                "live_connection_verified":False, "readiness":self._readiness()}
    def _readiness(self) -> str:
        if not self._module.get("enabled",True): return Readiness.DISABLED.value
        value=self._module.get("status",Readiness.CATALOG_ONLY.value)
        if value in (Readiness.READY.value,Readiness.ADAPTER_SCAFFOLD.value): return value
        return Readiness.CATALOG_ONLY.value
    def capabilities(self) -> dict[str,Any]:
        values=self._module.get("capabilities",[])
        return {"success":True,"ecosystem_id":self.ECOSYSTEM_ID,"count":len(values),
                "capabilities":[{"name":v,"authorization_class":AdobeCorePolicy.classify_capability(v)} for v in values]}
    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str,Any]:
        try:
            AdobeCorePolicy.require_tenant_context(context)
            AdobeCorePolicy.validate_capability(self._module,capability)
        except (ValueError,PermissionError) as exc:
            return CoreResult(False,self.ECOSYSTEM_ID,"POLICY_DENIED",
                errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
        return CoreResult(True,self.ECOSYSTEM_ID,"CORE_POLICY_PASSED_PROVIDER_AUTH_STILL_REQUIRED",
            data={"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,
                  "authorization_class":AdobeCorePolicy.classify_capability(capability),"api_call_performed":False},
            request_id=context.request_id).to_dict()
