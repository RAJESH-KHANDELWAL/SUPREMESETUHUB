"""Canonical NSFWinfra Core manager and read-only master catalog access."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .domain_runtime import NSFWinfraCoreDomainManager
from .orchestrator import NSFWinfraCoreOrchestrator
from .service import NSFWinfraCoreEcosystemService

MASTER_CATALOG_PATH = Path(__file__).resolve().parents[4] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
CANONICAL_ENTRY_IDS = (
    "S09_cloud_computing",
    "S10_global_infrastructure",
    "S10_global_ai_core",
    "S12_ai_research",
)


def master_catalog_reference() -> dict[str, Any]:
    """Return read-only metadata for the shared master catalog."""
    try:
        data = json.loads(MASTER_CATALOG_PATH.read_text(encoding="utf-8"))
        expansion = data.get("expansion", {})
        present = {
            entry: any(
                entry == item.get("entry_id")
                for section in data.get("sections", [])
                for item in section.get("entries", [])
            )
            for entry in CANONICAL_ENTRY_IDS
        }
        return {
            "available": True,
            "catalogue_id": data.get("catalogue_id"),
            "source_path": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
            "target_unique_entries": expansion.get("target_unique_entries"),
            "current_unique_entries": expansion.get("current_unique_entries"),
            "remaining_unique_entries": expansion.get("remaining_unique_entries"),
            "canonical_entry_ids": list(CANONICAL_ENTRY_IDS),
            "mapped_entry_presence": present,
            "access_mode": "READ_ONLY",
            "catalogue_mutated": False,
            "catalogue_entries_added": 0,
        }
    except (OSError, ValueError) as exc:
        return {
            "available": False,
            "source_path": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
            "status": "MASTER_CATALOG_UNAVAILABLE",
            "error_type": type(exc).__name__,
            "access_mode": "READ_ONLY",
            "catalogue_mutated": False,
        }


class NSFWinfraCoreManager:
    NAME = "NSFW INFRA CORE ECOSYSTEM"
    ECOSYSTEM_ID = "NSFWINFRA-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = NSFWinfraCoreOrchestrator()
        self._service = NSFWinfraCoreEcosystemService()

    def status(self) -> dict[str, Any]:
        result = self._service.status()
        result["master_catalog"] = self.master_catalog()
        return result

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.products(enabled_only)

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._orchestrator.product(ecosystem_id)

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def list_offerings(self) -> dict[str, Any]:
        return self._orchestrator.offerings()

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

    def master_catalog(self) -> dict[str, Any]:
        return master_catalog_reference()

    def get_domain_manager(self, domain_id: str) -> NSFWinfraCoreDomainManager:
        return NSFWinfraCoreDomainManager(domain_id)


def get_manager() -> NSFWinfraCoreManager:
    return NSFWinfraCoreManager()


__all__ = [
    "NSFWinfraCoreManager",
    "get_manager",
    "MASTER_CATALOG_PATH",
    "CANONICAL_ENTRY_IDS",
    "master_catalog_reference",
]
