"""Canonical manager for the Global AI Core Ecosystem.

The manager owns AI provider/domain metadata discovery only. Authentication,
provider transport, inference, agent execution, persistence and scheduling
remain in their API, ENGINE, DATABASE and STORAGE layers.
"""
from __future__ import annotations

from typing import Any

from .domain_runtime import GlobalAICoreDomainManager
from .ecosystem_service import GlobalAICoreEcosystemService
from .orchestrator import GlobalAICoreOrchestrator


class GlobalAICoreManager:
    """Stable Google Core-style entry point for Global AI metadata."""

    NAME = "GLOBAL AI CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-AI-CORE-ECOSYSTEM"
    MASTER_CATALOG_REF = "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    MASTER_CATALOG_TARGET_UNIQUE_ENTRIES = 2468
    MASTER_CATALOG_OWNER_LAYER = "GLOBAL_ENGINE_ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = GlobalAICoreOrchestrator()
        self._service = GlobalAICoreEcosystemService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_products(enabled_only=enabled_only)

    def get_product(self, provider_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(provider_id)

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def list_offerings(self) -> dict[str, Any]:
        return self._orchestrator.offerings()

    def get_offering(self, provider_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_offering(provider_id)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

    def get_domain_manager(self, domain_id: str) -> GlobalAICoreDomainManager:
        return GlobalAICoreDomainManager(domain_id)

    def master_catalog_reference(self) -> dict[str, Any]:
        """Expose the 2,468-entry master-catalog pointer without owning/loading it."""
        return {
            "catalogue_id": "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM",
            "source_path": self.MASTER_CATALOG_REF,
            "owner_layer": self.MASTER_CATALOG_OWNER_LAYER,
            "target_unique_entries": self.MASTER_CATALOG_TARGET_UNIQUE_ENTRIES,
            "loaded_by_global_ai_core": False,
            "ownership_note": (
                "The master planning catalog is owned by Global Engine. "
                "Its entries are not Global AI provider records."
            ),
        }


def get_manager() -> GlobalAICoreManager:
    """Return the canonical Global AI Core manager."""
    return GlobalAICoreManager()


__all__ = ["GlobalAICoreManager", "get_manager"]
