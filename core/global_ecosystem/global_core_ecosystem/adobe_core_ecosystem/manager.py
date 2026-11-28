"""Canonical manager entry point for the Adobe Core Ecosystem."""
from __future__ import annotations
from typing import Any
from .orchestrator import AdobeCoreOrchestrator
from .domain_runtime import AdobeCoreDomainManager
from .service import AdobeCoreEcosystemService

class AdobeCoreManager:
    NAME = "ADOBE CORE ECOSYSTEM"
    ECOSYSTEM_ID = "ADOBE-CORE-ECOSYSTEM"
    def __init__(self) -> None:
        self._orchestrator = AdobeCoreOrchestrator()
        self._service = AdobeCoreEcosystemService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def health(self) -> dict[str, Any]: return self._orchestrator.health()
    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_products(enabled_only=enabled_only)
    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(ecosystem_id)
    def list_domains(self) -> dict[str, Any]: return self._orchestrator.domains()
    def list_domain_inventory(self) -> list[dict[str, Any]]: return self._orchestrator.domain_inventory()
    def dependency_map(self) -> dict[str, Any]: return self._orchestrator.dependency_map()
    def manager_status(self) -> dict[str, Any]: return self._service.manager_status()
    def list_registered_modules(self) -> dict[str, Any]: return self._service.list_registered_modules()
    def get_domain_manager(self, domain_id: str) -> AdobeCoreDomainManager:
        return AdobeCoreDomainManager(domain_id)

def get_manager() -> AdobeCoreManager:
    return AdobeCoreManager()

__all__ = ["AdobeCoreManager", "get_manager"]
