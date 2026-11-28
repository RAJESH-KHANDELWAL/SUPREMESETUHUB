"""Google CORE-aligned manager for affiliate marketing business metadata."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .catalog import list_platforms
from .module_service import AffiliatePlatformModuleService

class GlobalAffiliateMarketingCoreManager:
    ECOSYSTEM_ID = "GLOBAL-AFFILIATE-MARKETING-BUSINESS-CORE-ECOSYSTEM"
    VERSION = "1.0.0"
    MASTER_CATALOG_PATH = Path(__file__).resolve().parents[5] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    MASTER_CATALOG_ID = "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"
    MASTER_CATALOG_TARGET = 2468

    def __init__(self) -> None:
        self.modules = AffiliatePlatformModuleService()

    def status(self) -> dict[str, Any]:
        module_status = self.modules.status()
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "name": "GLOBAL AFFILIATE MARKETING BUSINESS CORE ECOSYSTEM",
            "layer": "CORE",
            "version": self.VERSION,
            "status": "FOUNDATION_READY",
            "platform_count": module_status["platform_count"],
            "program_platform_count": module_status["program_platform_count"],
            "network_candidate_count": module_status["network_candidate_count"],
            "verified_program_count": module_status["verified_program_count"],
            "live_connections_verified": False,
            "master_catalog": self.master_catalog_reference(),
        }

    def list_platforms(self, *, region: str | None = None, include_candidates: bool = True) -> list[dict[str, Any]]:
        return list_platforms(region=region, include_candidates=include_candidates)

    def master_catalog_reference(self) -> dict[str, Any]:
        return {
            "catalogue_id": self.MASTER_CATALOG_ID,
            "source_path": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
            "owner_layer": "GLOBAL_ENGINE_ECOSYSTEM",
            "access_mode": "READ_ONLY_ON_DEMAND",
            "target_unique_entries": self.MASTER_CATALOG_TARGET,
        }

    def master_catalog_inventory(self) -> dict[str, Any]:
        """Read and validate the existing master catalog without modifying it."""
        if not self.MASTER_CATALOG_PATH.is_file():
            raise FileNotFoundError("GLOBAL_SUPREME_MASTER_CATALOG_NOT_FOUND")
        catalog = json.loads(self.MASTER_CATALOG_PATH.read_text(encoding="utf-8"))
        if catalog.get("catalogue_id") != self.MASTER_CATALOG_ID:
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_ID_MISMATCH")
        entries: list[dict[str, Any]] = []
        for section in catalog.get("sections", []):
            for entry in section.get("entries", []):
                entries.append({
                    **entry,
                    "section_id": section.get("section_id"),
                    "section_title": section.get("title"),
                })
        counts = catalog.get("counts", {})
        expansion = catalog.get("expansion", {})
        cross_refs = sum(entry.get("entry_kind") == "cross_reference" for entry in entries)
        unique_count = len(entries) - cross_refs
        target = expansion.get("target_unique_entries")
        if len(catalog.get("sections", [])) != counts.get("section_count"):
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_SECTION_COUNT_MISMATCH")
        if len(entries) != counts.get("source_numbered_entries"):
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_SOURCE_COUNT_MISMATCH")
        if cross_refs != counts.get("cross_reference_entries"):
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_REFERENCE_COUNT_MISMATCH")
        if unique_count != counts.get("unique_catalogue_entries"):
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_UNIQUE_COUNT_MISMATCH")
        if unique_count != expansion.get("current_unique_entries"):
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_EXPANSION_COUNT_MISMATCH")
        if target != self.MASTER_CATALOG_TARGET or expansion.get("remaining_unique_entries") != target - unique_count:
            raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_TARGET_OR_REMAINING_MISMATCH")
        affiliate_entries = [entry for entry in entries if entry.get("entry_id") == "S08_affiliate_business"]
        return {
            "success": True,
            "catalogue_id": catalog["catalogue_id"],
            "source_path": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
            "access_mode": "READ_ONLY",
            "target_unique_entries": target,
            "current_unique_entries": unique_count,
            "remaining_unique_entries": target - unique_count,
            "source_numbered_entries": len(entries),
            "cross_reference_entries": cross_refs,
            "section_count": len(catalog["sections"]),
            "affiliate_business_entries": affiliate_entries,
            "entries": entries,
        }

    def get_master_catalog_entry(self, entry_id: str) -> dict[str, Any] | None:
        if not isinstance(entry_id, str) or not entry_id.strip():
            return None
        return next(
            (entry for entry in self.master_catalog_inventory()["entries"] if entry.get("entry_id") == entry_id.strip()),
            None,
        )

def get_manager() -> GlobalAffiliateMarketingCoreManager:
    return GlobalAffiliateMarketingCoreManager()

__all__ = ["GlobalAffiliateMarketingCoreManager", "get_manager"]
