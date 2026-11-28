"""Global People Life CORE Ecosystem read-only control-plane service."""
from __future__ import annotations
from typing import Any
from .catalog import get_people_life_core_catalog, SERVICE_TIERS
from .orchestrator import PeopleLifeCoreOrchestrator

class PeopleLifeCoreEcosystemService:
    NAME = "GLOBAL PEOPLE LIFE CORE ECOSYSTEM"

    def __init__(self) -> None:
        self.orchestrator = PeopleLifeCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        catalog = get_people_life_core_catalog()
        health = self.orchestrator.health()
        registry = self.manager_status()
        return {
            "success": True, "ecosystem_id": catalog["ecosystem_id"],
            "name": self.NAME, "status": catalog["status"],
            "registry_status": registry["registered"],
            "module_count": len(catalog["children"]),
            "domain_count": health["domain_count"],
            "local_domain_package_count": health["local_domain_package_count"],
            "cross_ecosystem_domain_reference_count": health["cross_ecosystem_domain_reference_count"],
            "age_restricted_domain_count": health["age_restricted_domain_count"],
            "service_tier_count": len(SERVICE_TIERS),
            "live_service_connections_verified": False,
            "application_workflows_executed": 0,
            "health": health, "manager_registration": registry,
        }

    def list_modules(self) -> dict[str, Any]:
        return self.orchestrator.list_modules()

    def list_domains(self) -> dict[str, Any]:
        return self.orchestrator.domains()

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self.orchestrator.domain_inventory()

    def get_module(self, module_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_module(module_id)

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_domain(domain_id)

    def health(self) -> dict[str, Any]:
        return self.orchestrator.health()

    def dependency_map(self) -> dict[str, Any]:
        return self.orchestrator.dependency_map()

    def manager_status(self) -> dict[str, Any]:
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            manager = GlobalEcosystemManager()
            record = manager.get("GLOBAL-PEOPLE-LIFE-CORE-ECOSYSTEM")
        except Exception as exc:
            return {"success": False, "registered": False, "ecosystem": None, "error": type(exc).__name__}
        return {"success": record is not None, "registered": record is not None, "ecosystem": record, "live_service_connections_verified": False}
