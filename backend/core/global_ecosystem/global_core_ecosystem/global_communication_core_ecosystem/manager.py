"""Canonical manager for Global Communication Core metadata."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from .catalog import get_communication_core_catalog
from .domain_runtime import CommunicationCoreDomainManager
from .module_service import CommunicationProviderCoreService
from .orchestrator import CommunicationCoreOrchestrator
from .service import CommunicationCoreEcosystemService

class CommunicationCoreManager:
    NAME = "GLOBAL COMMUNICATION CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self) -> None:
        self._orchestrator = CommunicationCoreOrchestrator()
        self._service = CommunicationCoreEcosystemService()

    @staticmethod
    def master_catalog_path() -> Path:
        return Path(__file__).resolve().parents[4] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"

    def master_catalog_summary(self) -> dict[str, Any]:
        path = self.master_catalog_path()
        if not path.is_file():
            return {"available": False, "status": "MASTER_CATALOG_NOT_FOUND", "read_only": True}
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {"available": False, "status": "MASTER_CATALOG_INVALID", "read_only": True}
        expansion, counts = data.get("expansion", {}), data.get("counts", {})
        index = data.get("ecosystem_module_index", {})
        registered = any(item.get("ecosystem_id") == self.ECOSYSTEM_ID
                         for item in index.get("modules", []))
        return {
            "available": True, "catalogue_id": data.get("catalogue_id"),
            "target_unique_entries": expansion.get("target_unique_entries"),
            "current_unique_entries": expansion.get("current_unique_entries"),
            "remaining_unique_entries": expansion.get("remaining_unique_entries"),
            "section_count": counts.get("section_count"),
            "unique_catalogue_entries": counts.get("unique_catalogue_entries"),
            "module_index_registered": registered, "read_only": True,
        }

    def catalog(self) -> dict[str, Any]:
        return get_communication_core_catalog()

    def status(self) -> dict[str, Any]:
        return {**self._service.status(), "version": self.VERSION,
                "master_catalog": self.master_catalog_summary(), "inventory": self.health()}

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_products(enabled_only=enabled_only)

    def list_providers(self, *, family: str | None = None, region: str | None = None) -> dict[str, Any]:
        return self._orchestrator.list_providers(family=family, region=region)

    def get_product(self, product_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(product_id)

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()

    def get_domain_manager(self, domain_id: str) -> CommunicationCoreDomainManager:
        return CommunicationCoreDomainManager(domain_id)

    def get_provider_service(self, provider_id: str) -> CommunicationProviderCoreService:
        return CommunicationProviderCoreService(provider_id)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

_manager_instance: CommunicationCoreManager | None = None

def get_manager() -> CommunicationCoreManager:
    """Return the shared canonical manager instance."""
    global _manager_instance
    if _manager_instance is None:
        _manager_instance = CommunicationCoreManager()
    return _manager_instance

__all__ = ["CommunicationCoreManager", "get_manager"]
