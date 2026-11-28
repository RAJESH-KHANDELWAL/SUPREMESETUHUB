"""Canonical manager for Global Cloud Core.

Owns provider/workload discovery, cloud capability classification and a
read-only on-demand bridge to the cross-ecosystem master planning catalog.
It does not provision infrastructure, call cloud APIs, store credentials,
execute workloads or persist application data.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

from .domain_catalog import CLOUD_DOMAIN_DEFINITIONS, cloud_domain_summary, list_cloud_domain_inventory
from .domain_runtime import GlobalCloudCoreDomainManager
from .service import GlobalCloudCoreService


class GlobalCloudCoreManager:
    NAME = "GLOBAL CLOUD CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-CLOUD-CORE-ECOSYSTEM"
    MASTER_CATALOG_REF = "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    MASTER_CATALOG_ID = "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"
    MASTER_CATALOG_OWNER_LAYER = "GLOBAL_ENGINE_ECOSYSTEM"
    MASTER_CATALOG_TARGET_UNIQUE_ENTRIES = 2468

    def __init__(self) -> None:
        self._service = GlobalCloudCoreService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._service.health()

    def list_products(self, *, origin: str | None = None) -> dict[str, Any]:
        return self._service.list_products(origin=origin)

    def get_product(self, provider_id: str) -> dict[str, Any] | None:
        return self._service.get_product(provider_id)

    def list_domains(self) -> dict[str, Any]:
        return cloud_domain_summary()

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return list_cloud_domain_inventory()

    def get_domain_manager(self, domain_id: str) -> GlobalCloudCoreDomainManager:
        return GlobalCloudCoreDomainManager(domain_id)

    def list_offerings(self, *, tier: str | None = None,
                       region: str | None = None,
                       adult_industry: bool | None = None) -> dict[str, Any]:
        return self._service.list_offerings(tier=tier, region=region, adult_industry=adult_industry)

    def get_offering(self, workload_id: str) -> dict[str, Any] | None:
        return self._service.get_offering(workload_id)

    def list_scopes(self) -> dict[str, Any]:
        return self._service.list_scopes()

    def list_capabilities(self) -> dict[str, Any]:
        return self._service.list_capabilities()

    def dependency_map(self) -> dict[str, Any]:
        return self._service.dependency_map()

    @classmethod
    def _master_catalog_path(cls) -> Path:
        return Path(__file__).resolve().parents[5] / cls.MASTER_CATALOG_REF

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
        return {
            "catalogue_id": self.MASTER_CATALOG_ID,
            "source_path": self.MASTER_CATALOG_REF,
            "owner_layer": self.MASTER_CATALOG_OWNER_LAYER,
            "target_unique_entries": self.MASTER_CATALOG_TARGET_UNIQUE_ENTRIES,
            "access_mode": "READ_ONLY_ON_DEMAND",
            "source_of_truth": True,
            "loaded_by_reference_call": False,
            "ownership_note": "Global Engine remains the catalog owner; Cloud Core reads the source without copying or mutating it.",
        }

    def master_catalog_inventory(self, *, include_cross_references: bool = True) -> dict[str, Any]:
        catalog = self._load_master_catalog()
        all_entries: list[dict[str, Any]] = []
        sections: list[dict[str, Any]] = []
        for section in catalog["sections"]:
            visible = []
            for entry in section.get("entries", []):
                row = {**entry, "section_id": section.get("section_id"),
                       "section_title": section.get("title")}
                all_entries.append(row)
                if include_cross_references or row.get("entry_kind") != "cross_reference":
                    visible.append(row)
            sections.append({
                "section_number": section.get("section_number"),
                "section_id": section.get("section_id"),
                "title": section.get("title"),
                "entry_count": len(visible),
                "entries": visible,
            })
        counts, expansion = catalog.get("counts", {}), catalog.get("expansion", {})
        source_count = len(all_entries)
        cross_count = sum(row.get("entry_kind") == "cross_reference" for row in all_entries)
        unique_count = source_count - cross_count
        target = expansion.get("target_unique_entries")
        remaining = expansion.get("remaining_unique_entries")
        checks = (
            (unique_count, counts.get("unique_catalogue_entries"), "UNIQUE_COUNT"),
            (source_count, counts.get("source_numbered_entries"), "SOURCE_COUNT"),
            (cross_count, counts.get("cross_reference_entries"), "REFERENCE_COUNT"),
            (unique_count, expansion.get("current_unique_entries"), "EXPANSION_COUNT"),
            (target, self.MASTER_CATALOG_TARGET_UNIQUE_ENTRIES, "TARGET"),
            (remaining, target - unique_count if isinstance(target, int) else None, "REMAINING_COUNT"),
        )
        for actual, expected, label in checks:
            if actual != expected:
                raise ValueError("GLOBAL_SUPREME_MASTER_CATALOG_" + label + "_MISMATCH")
        return {
            "success": True, "catalogue_id": catalog["catalogue_id"],
            "title": catalog.get("title"), "source_path": self.MASTER_CATALOG_REF,
            "owner_layer": self.MASTER_CATALOG_OWNER_LAYER, "access_mode": "READ_ONLY",
            "target_unique_entries": target, "current_unique_entries": unique_count,
            "remaining_unique_entries": remaining, "source_numbered_entries": source_count,
            "cross_reference_entries": cross_count, "section_count": len(sections),
            "expansion_status": expansion.get("status"), "expansion_policy": expansion.get("policy"),
            "entries": all_entries if include_cross_references else [
                row for row in all_entries if row.get("entry_kind") != "cross_reference"
            ],
            "sections": sections,
        }

    def get_master_catalog_entry(self, entry_id: str) -> dict[str, Any] | None:
        needle = str(entry_id or "").strip()
        if not needle:
            return None
        return next((row for row in self.master_catalog_inventory()["entries"]
                     if row.get("entry_id") == needle), None)


def get_manager() -> GlobalCloudCoreManager:
    return GlobalCloudCoreManager()


__all__ = ["GlobalCloudCoreManager", "get_manager"]
