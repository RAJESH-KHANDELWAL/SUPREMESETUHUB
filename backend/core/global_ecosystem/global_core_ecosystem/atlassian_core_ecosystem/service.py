"""Atlassian Core provider control-plane facade."""
from __future__ import annotations
from typing import Any
from .catalog import get_atlassian_core_catalog
from .orchestrator import AtlassianCoreOrchestrator

class AtlassianCoreEcosystemService:
    NAME = "ATLASSIAN CORE ECOSYSTEM"
    def __init__(self) -> None: self.orchestrator = AtlassianCoreOrchestrator()
    def status(self) -> dict[str, Any]:
        catalog = get_atlassian_core_catalog(); health = self.orchestrator.health(); registry = self.manager_status()
        return {"success": True, "ecosystem_id": catalog["ecosystem_id"], "name": self.NAME, "provider": "atlassian", "status": catalog["status"], "registry_status": registry["registered"], "module_count": len(catalog["children"]), "domain_count": health["domain_count"], "runtime_offering_count": health["runtime_offering_count"], "connected_modules": 0, "live_connection_verified": False, "api_calls_performed": 0, "health": health, "api_catalog_ref": catalog["api_catalog_ref"]}
    def manager_status(self) -> dict[str, Any]:
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            record = GlobalEcosystemManager().get("GLOBAL-ATLASSIAN-CORE-ECOSYSTEM")
        except Exception as exc:
            return {"success": False, "registered": False, "ecosystem": None, "error": type(exc).__name__}
        return {"success": record is not None, "registered": record is not None, "ecosystem": record, "live_connection_verified": False}
    def list_modules(self): return self.orchestrator.list_products()
    def list_domains(self): return self.orchestrator.domains()
    def list_offerings(self): return self.orchestrator.offerings()
    def get_module(self, ecosystem_id: str): return self.orchestrator.get_product(ecosystem_id)
    def health(self): return self.orchestrator.health()
    def dependency_map(self): return self.orchestrator.dependency_map()
