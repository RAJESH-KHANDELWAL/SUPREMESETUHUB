"""Canonical read-only manager for Global APP Core."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

from backend.global_ecosystem.global_app_ecosystem import (
    get_app_provider, get_domain, get_scope_catalog, list_app_capability_groups,
    list_app_providers, list_app_types, list_domain_ids,
    validate_app_provider_registry,
)
from .service import GlobalAppCoreService


class GlobalAppCoreManager:
    NAME = "GLOBAL APP CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-APP-CORE-ECOSYSTEM"
    MASTER_CATALOG_REF = "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    MASTER_CATALOG_ID = "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"
    MASTER_CATALOG_OWNER_LAYER = "GLOBAL_ENGINE_ECOSYSTEM"
    MASTER_CATALOG_TARGET_UNIQUE_ENTRIES = 2468

    def __init__(self) -> None:
        self._service = GlobalAppCoreService()

    def status(self) -> dict[str, Any]:
        providers = list_app_providers()
        errors = validate_app_provider_registry()
        return {
            "success": not errors, "ecosystem_id": self.ECOSYSTEM_ID,
            "name": self.NAME, "layer": "CORE", "provider_count": len(providers),
            "domain_count": len(get_scope_catalog()["domains"]),
            "app_type_count": len(list_app_types()),
            "capability_group_count": len(list_app_capability_groups()),
            "provider_registry_valid": not errors,
            "provider_registry_errors": list(errors),
            "live_connections_verified": 0, "api_calls_performed": 0,
            "execution": "NOT_PERFORMED", "persistence": "NOT_PERFORMED",
        }

    def health(self) -> dict[str, Any]:
        result = self.status()
        return {**result, "status": "CATALOG_AVAILABLE" if result["success"] else "REGISTRY_INVALID",
                "live_connection_verified": False}

    def list_products(self, *, category: str | None = None,
                      origin: str | None = None,
                      ecosystem_kind: str | None = None) -> dict[str, Any]:
        products = list_app_providers(category=category, origin=origin,
                                      ecosystem_kind=ecosystem_kind)
        return {"success": True, "count": len(products), "products": list(products)}

    def get_product(self, provider_id: str) -> dict[str, Any] | None:
        try:
            return self._service.resolve_provider(provider_id)
        except KeyError:
            return None

    def validate_app_type(self, app_type_id: str) -> dict[str, Any]:
        return self._service.validate_app_type(app_type_id)

    def list_domains(self) -> dict[str, Any]:
        domains = get_scope_catalog()["domains"]
        return {"success": True, "domain_count": len(domains), "domains": domains}

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return [get_domain(domain_id) for domain_id in list_domain_ids()]

    def list_app_types(self) -> list[dict[str, Any]]:
        return list(list_app_types())

    def list_capability_groups(self) -> list[dict[str, Any]]:
        return list(list_app_capability_groups())

    def list_offerings(self) -> dict[str, Any]:
        return self.list_products()

    def get_offering(self, provider_id: str) -> dict[str, Any] | None:
        return self.get_product(provider_id)

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True, "core": self.ECOSYSTEM_ID,
            "dependencies": {
                "provider_catalog": "backend/global_ecosystem/global_app_ecosystem/providers.py",
                "application_execution": "APP / APPLICATION RUNTIME",
                "authentication_and_authorization": "AUTH / IDENTITY",
                "api_transport": "API ECOSYSTEM",
                "persistence": "DATABASE AND STORAGE ECOSYSTEMS",
                "background_execution": "ENGINE ECOSYSTEM",
                "master_catalog": self.MASTER_CATALOG_REF,
            },
            "core_execution": "NOT_PERFORMED", "core_persistence": "NOT_PERFORMED",
        }

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
            "catalogue_id": self.MASTER_CATALOG_ID, "source_path": self.MASTER_CATALOG_REF,
            "owner_layer": self.MASTER_CATALOG_OWNER_LAYER,
            "target_unique_entries": self.MASTER_CATALOG_TARGET_UNIQUE_ENTRIES,
            "access_mode": "READ_ONLY_ON_DEMAND", "source_of_truth": True,
            "loaded_by_reference_call": False,
        }

    def master_catalog_inventory(self, *, include_cross_references: bool = True) -> dict[str, Any]:
        catalog = self._load_master_catalog()
        entries, sections = [], []
        for section in catalog["sections"]:
            visible = []
            for entry in section.get("entries", []):
                row = {**entry, "section_id": section.get("section_id"),
                       "section_title": section.get("title")}
                entries.append(row)
                if include_cross_references or entry.get("entry_kind") != "cross_reference":
                    visible.append(row)
            sections.append({
                "section_number": section.get("section_number"),
                "section_id": section.get("section_id"), "title": section.get("title"),
                "entry_count": len(visible), "entries": visible,
            })
        counts, expansion = catalog.get("counts", {}), catalog.get("expansion", {})
        source_count = len(entries)
        cross_count = sum(x.get("entry_kind") == "cross_reference" for x in entries)
        unique_count = source_count - cross_count
        target, remaining = expansion.get("target_unique_entries"), expansion.get("remaining_unique_entries")
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
            "entries": entries if include_cross_references else [
                x for x in entries if x.get("entry_kind") != "cross_reference"
            ],
            "sections": sections,
        }

    def get_master_catalog_entry(self, entry_id: str) -> dict[str, Any] | None:
        needle = str(entry_id or "").strip()
        if not needle:
            return None
        return next((x for x in self.master_catalog_inventory()["entries"]
                     if x.get("entry_id") == needle), None)


def get_manager() -> GlobalAppCoreManager:
    return GlobalAppCoreManager()


__all__ = ["GlobalAppCoreManager", "get_manager"]
