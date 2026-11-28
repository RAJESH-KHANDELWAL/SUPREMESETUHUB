"""Canonical manager for the Global Developer Core Ecosystem."""
from __future__ import annotations
from typing import Any
from .orchestrator import DeveloperCoreOrchestrator
from .domain_runtime import DeveloperCoreDomainManager
from .service import DeveloperCoreEcosystemService

class GlobalDeveloperCoreManager:
    NAME="GLOBAL DEVELOPER CORE ECOSYSTEM"
    ECOSYSTEM_ID="GLOBAL-DEVELOPER-CORE-ECOSYSTEM"
    def __init__(self):
        self._orchestrator=DeveloperCoreOrchestrator()
        self._service=DeveloperCoreEcosystemService()
    def status(self) -> dict[str,Any]: return self._service.status()
    def health(self) -> dict[str,Any]: return self._orchestrator.health()
    def list_products(self, *, enabled_only: bool=False) -> dict[str,Any]: return self._orchestrator.list_products(enabled_only=enabled_only)
    def get_product(self, ecosystem_id: str) -> dict[str,Any] | None: return self._orchestrator.get_product(ecosystem_id)
    def list_domains(self) -> dict[str,Any]: return self._orchestrator.domains()
    def list_domain_inventory(self) -> list[dict[str,Any]]: return self._orchestrator.domain_inventory()
    def dependency_map(self) -> dict[str,Any]: return self._orchestrator.dependency_map()
    def get_domain_manager(self, domain_id: str) -> DeveloperCoreDomainManager: return DeveloperCoreDomainManager(domain_id)

_manager: GlobalDeveloperCoreManager | None = None
def get_manager() -> GlobalDeveloperCoreManager:
    global _manager
    if _manager is None: _manager=GlobalDeveloperCoreManager()
    return _manager
__all__=["GlobalDeveloperCoreManager","get_manager"]
