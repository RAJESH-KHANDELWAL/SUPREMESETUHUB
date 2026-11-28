"""Canonical manager for the Global AI Core Ecosystem.

The manager owns AI provider/domain metadata discovery and a read-only,
on-demand bridge to the cross-ecosystem master planning catalog. Authentication,
provider transport, inference, agent execution, persistence and scheduling remain
in their API, ENGINE, DATABASE and STORAGE layers.
"""
from __future__ import annotations

import json
from pathlib import Path
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
    MASTER_CATALOG_ID = "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"

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

    @classmethod
    def _master_catalog_path(cls) -> Path:
        repository_root = Path(__file__).resolve().parents[5]
        return repository_root / cls.MASTER_CATALOG_REF

    @classmethod
    def _load_master_catalog(cls) -> dict[str, Any]:
        path = cls._master_catalog_path()
        if not path.is_file():
            raise FileNotFoundError("GLOBAL_SUPREME_MASTER_CATALOG_NOT_FOUND: " + str(path))

        try:
            catalog = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_INVALID") from exc

        if catalog.get("catalogue_id") != cls.MASTER_CATALOG_ID:
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_ID_MISMATCH")
        if not isinstance(catalog.get("sections"), list):
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_SECTIONS_INVALID")
        return catalog

    def master_catalog_reference(self) -> dict[str, Any]:
        """Return source and ownership metadata without loading or copying the catalog."""
        return {
            "catalogue_id": self.MASTER_CATALOG_ID,
            "source_path": self.MASTER_CATALOG_REF,
            "owner_layer": self.MASTER_CATALOG_OWNER_LAYER,
            "target_unique_entries": self.MASTER_CATALOG_TARGET_UNIQUE_ENTRIES,
            "access_mode": "READ_ONLY_ON_DEMAND",
            "source_of_truth": True,
            "loaded_by_reference_call": False,
            "ownership_note": (
                "The master planning catalog remains owned by Global Engine. "
                "Global AI Core reads it on demand and does not duplicate or mutate it."
            ),
        }

    def master_catalog_inventory(
        self, *, include_cross_references: bool = True
    ) -> dict[str, Any]:
        """Read every currently defined master-catalog row without creating entries.

        The source contains numbered rows, including cross-reference rows. The
        catalog's own counts define unique entries separately from cross-references.
        """
        catalog = self._load_master_catalog()
        sections: list[dict[str, Any]] = []
        all_entries: list[dict[str, Any]] = []

        for section in catalog["sections"]:
            section_id = section.get("section_id")
            section_title = section.get("title")
            section_entries = []
            for entry in section.get("entries", []):
                normalized = {
                    **entry,
                    "section_id": section_id,
                    "section_title": section_title,
                }
                all_entries.append(normalized)
                if include_cross_references or entry.get("entry_kind") != "cross_reference":
                    section_entries.append(normalized)
            sections.append({
                "section_number": section.get("section_number"),
                "section_id": section_id,
                "title": section_title,
                "entry_count": len(section_entries),
                "entries": section_entries,
            })

        counts = catalog.get("counts", {})
        expansion = catalog.get("expansion", {})
        source_entry_count = len(all_entries)
        cross_reference_count = sum(
            entry.get("entry_kind") == "cross_reference" for entry in all_entries
        )
        unique_entry_count = source_entry_count - cross_reference_count

        if unique_entry_count != counts.get("unique_catalogue_entries"):
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_UNIQUE_COUNT_MISMATCH")
        if source_entry_count != counts.get("source_numbered_entries"):
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_SOURCE_COUNT_MISMATCH")
        if cross_reference_count != counts.get("cross_reference_entries"):
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_REFERENCE_COUNT_MISMATCH")
        if expansion.get("current_unique_entries") != unique_entry_count:
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_EXPANSION_COUNT_MISMATCH")
        target = expansion.get("target_unique_entries")
        remaining = expansion.get("remaining_unique_entries")
        if target != self.MASTER_CATALOG_TARGET_UNIQUE_ENTRIES:
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_TARGET_MISMATCH")
        if remaining != target - unique_entry_count:
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_REMAINING_COUNT_MISMATCH")

        return {
            "success": True,
            "catalogue_id": catalog["catalogue_id"],
            "title": catalog.get("title"),
            "source_path": self.MASTER_CATALOG_REF,
            "owner_layer": self.MASTER_CATALOG_OWNER_LAYER,
            "access_mode": "READ_ONLY",
            "target_unique_entries": target,
            "current_unique_entries": unique_entry_count,
            "remaining_unique_entries": remaining,
            "source_numbered_entries": source_entry_count,
            "cross_reference_entries": cross_reference_count,
            "section_count": len(sections),
            "expansion_status": expansion.get("status"),
            "expansion_policy": expansion.get("policy"),
            "entries": all_entries if include_cross_references else [
                entry for entry in all_entries
                if entry.get("entry_kind") != "cross_reference"
            ],
            "sections": sections,
        }

    def get_master_catalog_entry(self, entry_id: str) -> dict[str, Any] | None:
        """Find a source row by its exact entry_id, including cross-reference rows."""
        needle = str(entry_id).strip()
        if not needle:
            return None
        inventory = self.master_catalog_inventory(include_cross_references=True)
        return next(
            (entry for entry in inventory["entries"] if entry.get("entry_id") == needle),
            None,
        )


def get_manager() -> GlobalAICoreManager:
    """Return the canonical Global AI Core manager."""
    return GlobalAICoreManager()


__all__ = ["GlobalAICoreManager", "get_manager"]
