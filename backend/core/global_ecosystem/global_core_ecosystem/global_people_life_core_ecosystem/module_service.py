"""Reusable read-only service for a registered people-life domain."""
from __future__ import annotations
from typing import Any
from .catalog import get_people_life_core_catalog
from .contracts import CoreResult,Readiness,TenantContext
from .policy import PeopleLifePolicyError,classify_capability,require_tenant_context,safe_domain_summary,validate_capability

class PeopleLifeDomainCoreService:
    def __init__(self,domain_id: str) -> None:
        modules=get_people_life_core_catalog()["children"]
        self._domain=next((x for x in modules if x["domain_id"].casefold()==domain_id.strip().casefold()),None)
        if self._domain is None: raise LookupError(f"PEOPLE_LIFE_DOMAIN_NOT_REGISTERED: {domain_id}")
        self.ECOSYSTEM_ID=self._domain["ecosystem_id"]
    def describe(self) -> dict[str,Any]:
        return {"success":True,**safe_domain_summary(self._domain),"core_layer":"GLOBAL_PEOPLE_LIFE_CORE","application_workflows_in_core":False,"live_service_verified":False}
    def readiness(self) -> dict[str,Any]:
        return {"domain_id":self._domain["domain_id"],"status":Readiness.CATALOG_ONLY.value,"catalog_ready":True,"application_configuration_required":True,"live_service":False,"api_calls_performed":0}
    def capabilities(self) -> dict[str,Any]:
        items=self._domain.get("capabilities",[])
        return {"success":True,"domain_id":self._domain["domain_id"],"count":len(items),"capabilities":[{"name":x,"authorization_class":classify_capability(x)} for x in items]}
    def authorize_capability(self,capability: str,context: TenantContext|None) -> dict[str,Any]:
        try:
            require_tenant_context(context); validate_capability(self._domain,capability,context)
        except (ValueError,PermissionError,PeopleLifePolicyError) as exc:
            return CoreResult(False,self.ECOSYSTEM_ID,"POLICY_DENIED",errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
        return CoreResult(True,self.ECOSYSTEM_ID,"CORE_POLICY_PASSED_APPLICATION_AUTHORIZATION_STILL_REQUIRED",
          data={"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,"authorization_class":classify_capability(capability),"workflow_executed":False},
          request_id=context.request_id).to_dict()
