"""Read-only metadata service for a registered developer platform."""
from __future__ import annotations
from typing import Any
from .manager import get_global_developer_core_catalog
from .contracts import CoreResult, TenantContext
from .policy import DeveloperCorePolicy

class DeveloperProviderCoreService:
    def __init__(self, ecosystem_id: str):
        self.ecosystem_id=ecosystem_id.strip().casefold()
        self.module=next((x for x in get_global_developer_core_catalog()["children"] if x["ecosystem_id"].casefold()==self.ecosystem_id),None)
        if self.module is None: raise LookupError(f"DEVELOPER_MODULE_NOT_REGISTERED: {ecosystem_id}")
    def status(self) -> dict[str,Any]:
        return {**DeveloperCorePolicy.safe_module_summary(self.module),"success":True,"core_layer":"GLOBAL_DEVELOPER_CORE","live_connection_verified":False,"api_calls_performed":0}
    def authorize_capability(self, capability: str, context: TenantContext | None, *, authorized: bool=False) -> dict[str,Any]:
        try:
            DeveloperCorePolicy.require_tenant_context(context)
            DeveloperCorePolicy.validate_capability(self.module,capability)
            DeveloperCorePolicy.require_explicit_authorization(capability,authorized)
        except (ValueError,PermissionError) as exc:
            return CoreResult(False,self.module["ecosystem_id"],"POLICY_DENIED",errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
        return CoreResult(True,self.module["ecosystem_id"],"CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED",data={"capability":capability,"api_call_performed":False},request_id=context.request_id).to_dict()
