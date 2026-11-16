"""Public read-only Global Domain Core ecosystem service."""
from __future__ import annotations
from typing import Any
from .catalog import get_domain_core_catalog
from .orchestrator import GlobalDomainCoreOrchestrator

class GlobalDomainCoreEcosystemService:
    NAME = "GLOBAL DOMAIN CORE ECOSYSTEM"

    def __init__(self) -> None:
        self.orchestrator = GlobalDomainCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        catalog = get_domain_core_catalog()
        health = self.orchestrator.health()
        registry = self.manager_status()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "name": self.NAME,
            "status": catalog["status"],
            "registry_status": registry["registered"],
            "provider_count": health["provider_count"],
            "domain_count": health["domain_count"],
            "connected_providers": 0,
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "health": health,
            "api_catalog_ref": catalog["api_catalog_ref"],
        }

    def manager_status(self) -> dict[str, Any]:
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            manager = GlobalEcosystemManager()
            record = manager.get("GLOBAL-DOMAIN-CORE-ECOSYSTEM")
        except Exception as exc:
            return {"success": False, "registered": False, "ecosystem": None,
                    "error": type(exc).__name__}
        return {"success": record is not None, "registered": record is not None,
                "ecosystem": record, "live_connection_verified": False}

    def list_providers(self) -> dict[str, Any]:
        return self.orchestrator.list_providers()

    def list_domains(self) -> dict[str, Any]:
        return self.orchestrator.domains()

    def list_inventory(self) -> dict[str, Any]:
        return self.orchestrator.inventory()

    def list_capability_packages(self) -> dict[str, Any]:
        return self.orchestrator.capability_packages()

    def health(self) -> dict[str, Any]:
        return self.orchestrator.health()

    def get_provider(self, provider_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_provider(provider_id)

    def dependency_map(self) -> dict[str, Any]:
        return self.orchestrator.dependency_map()
