"""Canonical manager for GLOBAL WEBSITE CORE ECOSYSTEM."""
from __future__ import annotations
from typing import Any
from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME
from .domain_catalog import get_domain
from .domain_runtime import WebsiteCoreDomainManager
from .orchestrator import WebsiteCoreOrchestrator
from .service import WebsiteCoreEcosystemService

class GlobalWebsiteCoreManager:
    NAME = ECOSYSTEM_NAME
    ECOSYSTEM_ID = ECOSYSTEM_ID

    def __init__(self) -> None:
        self._orchestrator = WebsiteCoreOrchestrator()
        self._service = WebsiteCoreEcosystemService()

    def status(self) -> dict[str, Any]: return self._service.status()
    def health(self) -> dict[str, Any]: return self._orchestrator.health()
    def catalog(self) -> dict[str, Any]: return self._orchestrator.catalog()
    def list_providers(self) -> list[dict[str, Any]]: return self._orchestrator.providers()
    def get_provider(self, provider_id: str) -> dict[str, Any] | None: return self._orchestrator.provider(provider_id)
    def list_products(self) -> list[dict[str, Any]]: return self._orchestrator.product_families()
    def get_product(self, family_id: str) -> dict[str, Any] | None: return self._orchestrator.product_family(family_id)
    def list_domains(self) -> list[dict[str, Any]]: return self._orchestrator.domains()
    def list_domain_inventory(self) -> list[dict[str, Any]]: return self._orchestrator.domains()
    def get_domain(self, domain_id: str) -> dict[str, Any] | None: return get_domain(domain_id)
    def get_domain_manager(self, domain_id: str) -> WebsiteCoreDomainManager:
        return WebsiteCoreDomainManager(domain_id)
    def dependency_map(self) -> dict[str, Any]: return self._orchestrator.dependency_map()

def get_manager() -> GlobalWebsiteCoreManager:
    return GlobalWebsiteCoreManager()

__all__ = ["GlobalWebsiteCoreManager", "get_manager"]
