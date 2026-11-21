"""Canonical read-only manager for GLOBAL SERVER CORE ECOSYSTEM.

CORE owns provider-neutral catalogs, domain contracts and readiness metadata.
This module never provisions infrastructure or contacts cloud providers.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .domain_registry import load_domain_registry
from .provider_catalog import get_provider_catalog
from .scope_catalog import (
    get_geographic_scope_catalog,
    get_service_tier_catalog,
    get_workload_domain_catalog,
)

ROOT = Path(__file__).resolve().parent
MASTER_CATALOG_PATH = ROOT.parents[4] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"EXPECTED_JSON_OBJECT: {path.name}")
    return value


def load_master_catalog() -> dict[str, Any]:
    return _load_json(MASTER_CATALOG_PATH)


def _manifest_for(domain: dict[str, Any]) -> dict[str, Any]:
    path = ROOT / domain["directory"] / "domain_manifest.json"
    manifest = _load_json(path)
    if manifest.get("domain_id") != domain["domain_id"]:
        raise ValueError(f"SERVER_DOMAIN_MANIFEST_ID_MISMATCH: {domain['domain_id']}")
    if manifest.get("parent_id") != "GLOBAL-SERVER-CORE-ECOSYSTEM":
        raise ValueError(f"SERVER_DOMAIN_MANIFEST_PARENT_MISMATCH: {domain['domain_id']}")
    return manifest


def validate_master_alignment() -> dict[str, Any]:
    registry = load_domain_registry()
    master = load_master_catalog()
    entry_sections = {
        entry["entry_id"]: section["section_id"]
        for section in master.get("sections", [])
        for entry in section.get("entries", [])
        if entry.get("entry_id")
    }
    refs: list[str] = []
    for domain in registry["domains"]:
        manifest = _manifest_for(domain)
        domain_refs = domain.get("master_catalog_refs", [])
        if not domain_refs or len(domain_refs) != len(set(domain_refs)):
            raise ValueError(f"SERVER_MASTER_REFS_MISSING_OR_DUPLICATE: {domain['domain_id']}")
        manifest_refs = manifest.get("master_catalog_refs", [])
        if set(domain_refs) != set(manifest_refs):
            raise ValueError(f"SERVER_MASTER_REFS_MANIFEST_MISMATCH: {domain['domain_id']}")
        if any(ref not in entry_sections for ref in domain_refs):
            raise ValueError(f"SERVER_MASTER_REF_UNKNOWN: {domain['domain_id']}")
        refs.extend(domain_refs)
    expansion = master.get("expansion", {})
    return {
        "success": True,
        "source": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
        "current_unique_entries": expansion.get("current_unique_entries"),
        "target_unique_entries": expansion.get("target_unique_entries"),
        "remaining_unique_entries": expansion.get("remaining_unique_entries"),
        "reference_occurrences": len(refs),
        "unique_references": len(set(refs)),
        "unknown_references": 0,
        "counts_as_new_master_entries": False,
    }


class GlobalServerCoreManager:
    """Discover and validate server CORE metadata without remote execution."""

    def catalog(self) -> dict[str, Any]:
        from .catalog import get_catalog
        return get_catalog()

    def list_domains(self) -> list[dict[str, Any]]:
        registry = load_domain_registry()
        return [_manifest_for(domain) for domain in registry["domains"]]

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        key = str(domain_id).strip().upper()
        for domain in self.list_domains():
            if domain["domain_id"] == key:
                return domain
        return None

    def list_providers(self) -> list[dict[str, Any]]:
        return get_provider_catalog()

    def list_workloads(self) -> list[dict[str, Any]]:
        return get_workload_domain_catalog().get("domains", [])

    def geography(self) -> dict[str, Any]:
        return get_geographic_scope_catalog()

    def service_tiers(self) -> list[dict[str, Any]]:
        return get_service_tier_catalog().get("tiers", [])

    def master_catalog_alignment(self) -> dict[str, Any]:
        return validate_master_alignment()

    def status(self) -> dict[str, Any]:
        registry = load_domain_registry()
        providers = get_provider_catalog()
        workloads = get_workload_domain_catalog().get("domains", [])
        tiers = get_service_tier_catalog().get("tiers", [])
        domains = self.list_domains()
        alignment = validate_master_alignment()
        return {
            "success": True,
            "ecosystem_id": "GLOBAL-SERVER-CORE-ECOSYSTEM",
            "layer": "CORE",
            "status": "CORE_CATALOG_AND_WORKLOAD_PROFILES",
            "provider_count": len(providers),
            "core_domain_count": len(registry["domains"]),
            "domain_manifest_count": len(domains),
            "control_area_count": sum(len(x.get("control_areas", [])) for x in domains),
            "workload_profile_count": len(workloads),
            "service_tier_count": len(tiers),
            "master_catalog_alignment": alignment,
            "live_provider_connections_verified": False,
            "remote_operations_enabled": False,
            "api_calls_performed": 0,
            "registry_persistence": "PROCESS_LOCAL_ONLY",
            "production_readiness_claimed": False,
        }


_MANAGER: GlobalServerCoreManager | None = None


def get_manager() -> GlobalServerCoreManager:
    global _MANAGER
    if _MANAGER is None:
        _MANAGER = GlobalServerCoreManager()
    return _MANAGER


def manager_status() -> dict[str, Any]:
    return get_manager().status()


__all__ = [
    "GlobalServerCoreManager",
    "get_manager",
    "manager_status",
    "load_master_catalog",
    "validate_master_alignment",
]
