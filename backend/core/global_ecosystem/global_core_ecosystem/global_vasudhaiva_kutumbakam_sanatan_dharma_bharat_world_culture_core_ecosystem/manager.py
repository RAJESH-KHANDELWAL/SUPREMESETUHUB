"""Stable manager for the Global Cultural Core Ecosystem.

The Core layer exposes cultural metadata and governance boundaries only.
Domain content, API transport, persistence and business execution remain in
their owning backend layers.
"""
from __future__ import annotations

from typing import Any

from .domain_runtime import CulturalCoreDomainManager
from .orchestrator import CulturalCoreOrchestrator
from .service import GlobalCulturalCore


class CulturalCoreManager:
    """Google-Core-aligned public entry point for cultural Core metadata."""

    NAME = (
        "GLOBAL VASUDHAIVA KUTUMBAKAM | SANATAN DHARMA | "
        "BHARAT SANSKRITI | WORLD CULTURE CORE ECOSYSTEM"
    )
    ECOSYSTEM_ID = (
        "GLOBAL-VASUDHAIVA-KUTUMBAKAM-SANATAN-DHARMA-"
        "BHARAT-WORLD-CULTURE-CORE-ECOSYSTEM"
    )

    def __init__(self) -> None:
        self._orchestrator = CulturalCoreOrchestrator()
        self._service = GlobalCulturalCore()

    def status(self) -> dict[str, Any]:
        """Return catalog and registry status without implying live connectivity."""
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def describe(self) -> dict[str, Any]:
        return self._service.describe()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        # In this domain ecosystem, registered domain packages are the products.
        return self._orchestrator.list_domains(enabled_only=enabled_only)

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_domain(ecosystem_id)

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.list_domains()

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def list_offerings(self) -> dict[str, Any]:
        return self._orchestrator.offerings()

    def get_offering(self, product_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_offering(product_id)

    def get_domain_manager(self, domain_id: str) -> CulturalCoreDomainManager:
        return self._service.get_domain_manager(domain_id)

    def knowledge(self) -> dict[str, Any]:
        return self._service.knowledge()

    def search(self, query: str) -> list[dict[str, Any]]:
        return self._service.search_foundation(query)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()


def get_manager() -> CulturalCoreManager:
    """Return the canonical manager factory, matching Google Core conventions."""
    return CulturalCoreManager()


__all__ = ["CulturalCoreManager", "get_manager"]
