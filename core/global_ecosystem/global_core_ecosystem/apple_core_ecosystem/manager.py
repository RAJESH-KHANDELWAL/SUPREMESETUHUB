"""Canonical entry point for Apple Core metadata and domain discovery."""
from __future__ import annotations
from typing import Any
from .orchestrator import AppleCoreOrchestrator
from .domain_runtime import AppleCoreDomainManager
from .service import AppleCoreEcosystemService

class AppleCoreManager:
    NAME = "APPLE CORE ECOSYSTEM"
    ECOSYSTEM_ID = "APPLE-CORE-ECOSYSTEM"
    def __init__(self) -> None:
        self._orchestrator = AppleCoreOrchestrator()
        self._service = AppleCoreEcosystemService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def health(self) -> dict[str, Any]: return self._orchestrator.health()
    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]: return self._orchestrator.list_products(enabled_only=enabled_only)
    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None: return self._orchestrator.get_product(ecosystem_id)
    def list_domains(self) -> dict[str, Any]: return self._orchestrator.domains()
    def list_domain_inventory(self) -> list[dict[str, Any]]: return self._orchestrator.domain_inventory()
    def list_offerings(self) -> dict[str, Any]: return self._orchestrator.offerings()
    def get_offering(self, product_id: str) -> dict[str, Any] | None: return self._orchestrator.get_offering(product_id)
    def dependency_map(self) -> dict[str, Any]: return self._orchestrator.dependency_map()
    def get_domain_manager(self, domain_id: str) -> AppleCoreDomainManager: return AppleCoreDomainManager(domain_id)

def get_manager() -> AppleCoreManager:
    return AppleCoreManager()
__all__ = ["AppleCoreManager", "get_manager"]
