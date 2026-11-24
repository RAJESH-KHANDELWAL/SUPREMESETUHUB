"""Reusable read-only service for programming-language domain metadata."""
from __future__ import annotations
from typing import Any
from .catalog import get_programming_language_core_catalog
from .contracts import CoreResult, Readiness, TenantContext
from .policy import ProgrammingLanguagePolicyError, classify_capability, require_tenant_context, safe_module_summary, validate_capability

class ProgrammingLanguageDomainCoreService:
    def __init__(self, domain_id: str) -> None:
        modules = get_programming_language_core_catalog()["children"]
        self._module = next((x for x in modules if x["domain_id"].casefold() == domain_id.strip().casefold()), None)
        if self._module is None:
            raise LookupError(f"PROGRAMMING_LANGUAGE_DOMAIN_NOT_REGISTERED: {domain_id}")
        self.ECOSYSTEM_ID = self._module["ecosystem_id"]

    def describe(self) -> dict[str, Any]:
        return {"success":True,**safe_module_summary(self._module),"core_layer":"GLOBAL_PROGRAMMING_LANGUAGE_CORE","runtime_execution_in_core":False,"live_runtime_verified":False}

    def readiness(self) -> dict[str, Any]:
        return {"domain_id":self._module["domain_id"],"status":Readiness.CATALOG_ONLY.value,"catalog_ready":True,"runtime_configuration_required":True,"runtime_execution":False,"api_calls_performed":0}

    def capabilities(self) -> dict[str, Any]:
        items=self._module.get("capabilities",[])
        return {"success":True,"domain_id":self._module["domain_id"],"count":len(items),"capabilities":[{"name":x,"authorization_class":classify_capability(x)} for x in items]}

    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str, Any]:
        try:
            require_tenant_context(context); validate_capability(self._module,capability)
        except (ValueError,PermissionError,ProgrammingLanguagePolicyError) as exc:
            return CoreResult(False,self.ECOSYSTEM_ID,"POLICY_DENIED",errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
        return CoreResult(True,self.ECOSYSTEM_ID,"CORE_POLICY_PASSED_RUNTIME_PERMISSION_STILL_REQUIRED",
            data={"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,"authorization_class":classify_capability(capability),"runtime_executed":False},
            request_id=context.request_id).to_dict()
