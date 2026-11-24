"""Canonical entry point for Global System Core Ecosystem."""
from __future__ import annotations
from typing import Any
from .domain_runtime import SystemCoreDomainManager
from .module_service import SystemProviderCoreService, SystemProductCoreService
from .orchestrator import SystemCoreOrchestrator
from .service import SystemCoreEcosystemService


class SystemCoreManager:
    NAME = "GLOBAL SYSTEM CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-SYSTEM-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = SystemCoreOrchestrator()
        self._service = SystemCoreEcosystemService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_providers(self) -> dict[str, Any]:
        return self._orchestrator.list_providers()

    def get_provider(self, provider_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_provider(provider_id)

    def list_products(self, *, provider_id: str | None = None, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_products(provider_id=provider_id, enabled_only=enabled_only)

    def get_product(self, product_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(product_id)

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def get_domain_manager(self, domain_id: str) -> SystemCoreDomainManager:
        return SystemCoreDomainManager(domain_id)

    def get_provider_manager(self, provider_id: str) -> SystemProviderCoreService:
        return SystemProviderCoreService(provider_id)

    def get_product_manager(self, product_id: str) -> SystemProductCoreService:
        return SystemProductCoreService(product_id)


def get_manager() -> SystemCoreManager:
    return SystemCoreManager()


__all__ = ["SystemCoreManager", "get_manager"]
