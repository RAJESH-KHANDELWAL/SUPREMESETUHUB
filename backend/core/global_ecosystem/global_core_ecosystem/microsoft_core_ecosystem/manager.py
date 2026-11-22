"""Canonical manager for Microsoft Core metadata."""
from __future__ import annotations
from typing import Any
from .orchestrator import MicrosoftCoreOrchestrator
from .domain_runtime import MicrosoftCoreDomainManager
from .service import MicrosoftCoreEcosystemService

class MicrosoftCoreManager:
    NAME = "MICROSOFT CORE ECOSYSTEM"
    ECOSYSTEM_ID = "MICROSOFT-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = MicrosoftCoreOrchestrator()
        self._service = MicrosoftCoreEcosystemService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_products(enabled_only=enabled_only)

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(ecosystem_id)

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

    def get_domain_manager(self, domain_id: str) -> MicrosoftCoreDomainManager:
        return MicrosoftCoreDomainManager(domain_id)

def get_manager() -> MicrosoftCoreManager:
    return MicrosoftCoreManager()

__all__ = ["MicrosoftCoreManager", "get_manager"]
