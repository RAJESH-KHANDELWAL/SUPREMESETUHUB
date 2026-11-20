"""Canonical manager for Global Communication Core Ecosystem.

Metadata-only facade. Provider OAuth, message delivery, telephony and storage
are deliberately outside this manager and require dedicated adapters.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from .orchestrator import CommunicationCoreOrchestrator
from .service import CommunicationCoreEcosystemService

class CommunicationCoreManager:
    NAME = "GLOBAL COMMUNICATION CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = CommunicationCoreOrchestrator()
        self._service = CommunicationCoreEcosystemService()

    @staticmethod
    def master_catalog_path() -> Path:
        return Path(__file__).resolve().parents[4] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"

    def master_catalog_summary(self) -> dict[str, Any]:
        path = self.master_catalog_path()
        if not path.is_file():
            return {"available": False, "status": "MASTER_CATALOG_NOT_FOUND"}
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {"available": False, "status": "MASTER_CATALOG_INVALID"}
        expansion = data.get("expansion", {})
        counts = data.get("counts", {})
        return {
            "available": True,
            "catalogue_id": data.get("catalogue_id"),
            "target_unique_entries": expansion.get("target_unique_entries"),
            "current_unique_entries": expansion.get("current_unique_entries"),
            "remaining_unique_entries": expansion.get("remaining_unique_entries"),
            "section_count": counts.get("section_count"),
            "unique_catalogue_entries": counts.get("unique_catalogue_entries"),
            "read_only": True,
        }

    def status(self) -> dict[str, Any]:
        return {**self._service.status(), "master_catalog": self.master_catalog_summary()}

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_products(enabled_only=enabled_only)

    def get_product(self, product_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(product_id)

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

def get_manager() -> CommunicationCoreManager:
    return CommunicationCoreManager()

__all__ = ["CommunicationCoreManager", "get_manager"]
