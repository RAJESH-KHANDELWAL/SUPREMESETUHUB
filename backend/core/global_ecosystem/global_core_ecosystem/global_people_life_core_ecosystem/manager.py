"""Canonical manager for the Global People Life CORE Ecosystem."""
from __future__ import annotations
from typing import Any
from .domain_runtime import PeopleLifeDomainManager
from .orchestrator import PeopleLifeCoreOrchestrator
from .service import PeopleLifeCoreEcosystemService

class PeopleLifeCoreManager:
    NAME = "GLOBAL PEOPLE LIFE CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-PEOPLE-LIFE-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = PeopleLifeCoreOrchestrator()
        self._service = PeopleLifeCoreEcosystemService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_modules(self) -> dict[str, Any]:
        return self._orchestrator.list_modules()

    def get_module(self, module_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_module(module_id)

    def list_domains(self, include_external: bool = True) -> dict[str, Any]:
        return self._orchestrator.list_domains(include_external=include_external)

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_domain(domain_id)

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

    def get_domain_manager(self, domain_id: str) -> PeopleLifeDomainManager:
        return PeopleLifeDomainManager(domain_id)

def get_manager() -> PeopleLifeCoreManager:
    return PeopleLifeCoreManager()

__all__ = ["PeopleLifeCoreManager", "PeopleLifeDomainManager", "get_manager"]
