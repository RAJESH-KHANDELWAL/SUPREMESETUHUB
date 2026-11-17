"""Global People Life CORE Ecosystem read-only control-plane service."""
from __future__ import annotations
from typing import Any
from .catalog import get_people_life_core_catalog
from .orchestrator import PeopleLifeCoreOrchestrator

class PeopleLifeCoreEcosystemService:
    NAME="GLOBAL PEOPLE LIFE CORE ECOSYSTEM"
    def __init__(self) -> None: self.orchestrator=PeopleLifeCoreOrchestrator()
    def status(self) -> dict[str,Any]:
        catalog=get_people_life_core_catalog(); health=self.orchestrator.health()
        return {"success":True,"ecosystem_id":catalog["ecosystem_id"],"name":self.NAME,"status":catalog["status"],
          "module_count":len(catalog["children"]),"domain_count":health["domain_count"],
          "age_restricted_domain_count":health["age_restricted_domain_count"],
          "live_service_connections_verified":False,"application_workflows_executed":0,"health":health}
    def list_modules(self) -> dict[str,Any]: return self.orchestrator.list_domains()
    def list_domains(self) -> dict[str,Any]: return self.orchestrator.domains()
    def get_module(self,domain_id: str) -> dict[str,Any]|None: return self.orchestrator.get_domain(domain_id)
    def health(self) -> dict[str,Any]: return self.orchestrator.health()
