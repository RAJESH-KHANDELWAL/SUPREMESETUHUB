"""Developer Core read-only control-plane service."""
from __future__ import annotations
from typing import Any
from .catalog import get_global_developer_core_catalog
from .orchestrator import DeveloperCoreOrchestrator

class DeveloperCoreEcosystemService:
    NAME="GLOBAL DEVELOPER CORE ECOSYSTEM"
    def __init__(self): self.orchestrator=DeveloperCoreOrchestrator()
    def status(self) -> dict[str,Any]:
        c=get_global_developer_core_catalog();h=self.orchestrator.health();registered=self.manager_status()
        return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":self.NAME,"status":c["status"],"registry_status":registered["registered"],"module_count":len(c["children"]),"domain_count":h["domain_count"],"live_connection_verified":False,"api_calls_performed":0,"health":h,"api_catalog_ref":c.get("api_catalog_ref")}
    def manager_status(self) -> dict[str,Any]:
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            record=GlobalEcosystemManager().get("GLOBAL-DEVELOPER-CORE-ECOSYSTEM")
            return {"success":record is not None,"registered":record is not None,"ecosystem":record,"live_connection_verified":False}
        except Exception as exc: return {"success":False,"registered":False,"ecosystem":None,"error":type(exc).__name__}
    def list_modules(self) -> dict[str,Any]: return self.orchestrator.list_products()
    def list_domains(self) -> dict[str,Any]: return self.orchestrator.domains()
    def get_module(self, ecosystem_id: str) -> dict[str,Any] | None: return self.orchestrator.get_product(ecosystem_id)
    def health(self) -> dict[str,Any]: return self.orchestrator.health()
    def dependency_map(self) -> dict[str,Any]: return self.orchestrator.dependency_map()
