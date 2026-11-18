"""People Life CORE discovery and policy-aware taxonomy orchestration."""
from __future__ import annotations
from typing import Any
from .catalog import get_people_life_core_catalog
from .domain_catalog import get_people_life_domain,list_people_life_domains,people_life_domain_summary
from .policy import safe_domain_summary

class PeopleLifeCoreOrchestrator:
    def catalog(self) -> dict[str,Any]: return get_people_life_core_catalog()
    def list_domains(self,enabled_only: bool=False) -> dict[str,Any]:
        items=self.catalog()["children"]
        if enabled_only: items=[x for x in items if x.get("enabled",True)]
        safe=[safe_domain_summary(x) for x in items]
        return {"success":True,"count":len(safe),"domains":safe}
    def get_domain(self,domain_id: str) -> dict[str,Any]|None: return get_people_life_domain(domain_id)
    def domains(self) -> dict[str,Any]:
        return {"success":True,**people_life_domain_summary(),"domains":list_people_life_domains()}
    def health(self) -> dict[str,Any]:
        catalog=self.catalog(); summary=people_life_domain_summary()
        return {"success":True,"ecosystem_id":catalog["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE",
          "domain_count":summary["domain_count"],"age_restricted_domain_count":summary["age_restricted_domain_count"],
          "enabled_domain_count":sum(bool(x.get("enabled",True)) for x in catalog["children"]),
          "live_service_connections_verified":0,"application_workflows_executed":0,
          "warning":"Taxonomy and policy metadata do not prove legal compliance, age verification, clinical suitability or a live service integration."}
