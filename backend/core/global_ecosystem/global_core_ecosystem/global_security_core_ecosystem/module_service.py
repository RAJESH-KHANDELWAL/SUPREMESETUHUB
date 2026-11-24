"""Read-only metadata service for one registered security provider."""
from __future__ import annotations
from typing import Any
from .contracts import CoreResult,TenantContext
from .constants import ECOSYSTEM_ID
from .policy import SecurityPolicyError,classify_capability,require_tenant_context,safe_provider_summary,validate_capability
from .provider_catalog import get_provider
class SecurityProviderCoreService:
    def __init__(self,provider_id:str):
        provider=get_provider(provider_id)
        if provider is None: raise LookupError(f"SECURITY_PROVIDER_NOT_REGISTERED: {provider_id}")
        self._provider=provider
    def describe(self):
        return {"success":True,**safe_provider_summary(self._provider),"api_transport_in_core":False,"live_connection_verified":False}
    def readiness(self):
        return {"provider_id":self._provider["provider_id"],"status":"CORE_CATALOG_ONLY","catalog_ready":True,"configuration_required":True,"live_connection":False,"api_calls_performed":0}
    def capabilities(self):
        items=self._provider["capabilities"]
        return {"success":True,"provider_id":self._provider["provider_id"],"count":len(items),"capabilities":[{"name":x,"authorization_class":classify_capability(x)} for x in items]}
    def authorize_capability(self,capability:str,context:TenantContext|None)->dict[str,Any]:
        try:
            require_tenant_context(context); validate_capability(self._provider,capability)
        except (ValueError,PermissionError,SecurityPolicyError) as exc:
            return CoreResult(False,self._provider["ecosystem_id"],"POLICY_DENIED",errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
        return CoreResult(True,self._provider["ecosystem_id"],"CORE_POLICY_PASSED_EXTERNAL_AUTHORIZATION_REQUIRED",data={"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,"authorization_class":classify_capability(capability),"provider_call_performed":False},request_id=context.request_id).to_dict()
