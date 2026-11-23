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
MASTER_CATALOG_PATH = ROOT.parents[3] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"


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
    module_index = master.get("ecosystem_module_index", {}).get("modules", [])
    module_matches = [
        item for item in module_index
        if item.get("ecosystem_id") == "GLOBAL-SERVER-CORE-ECOSYSTEM"
    ]
    implementation = master.get("implementation_registry", {}).get("global_server_core_ecosystem")
    if len(module_matches) != 1 or not implementation:
        raise ValueError("SERVER_MASTER_IMPLEMENTATION_REGISTRATION_MISSING")
    if implementation.get("master_catalog_unique_reference_count") != len(set(refs)):
        raise ValueError("SERVER_MASTER_IMPLEMENTATION_REFERENCE_COUNT_MISMATCH")
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
        manifests = [_manifest_for(domain) for domain in registry["domains"]]
        expected_root = (
            "backend/core/global_ecosystem/global_core_ecosystem/"
            "global_server_core_ecosystem/"
        )
        for domain, manifest in zip(registry["domains"], manifests):
            expected_path = expected_root + domain["directory"] + "/"
            if manifest.get("canonical_path") != expected_path:
                raise ValueError(f"SERVER_DOMAIN_CANONICAL_PATH_MISMATCH: {domain['domain_id']}")
            areas = manifest.get("control_areas", [])
            area_ids = [item.get("area_id") for item in areas]
            if (
                len(areas) != 6
                or any(not item.get("name") or not item.get("scope") for item in areas)
                or any(not area_id for area_id in area_ids)
                or len(area_ids) != len(set(area_ids))
            ):
                raise ValueError(f"SERVER_DOMAIN_CONTROL_AREAS_INVALID: {manifest['domain_id']}")
        expected_count = registry.get("domain_count")
        expected_area_count = registry.get("coverage", {}).get("control_area_count")
        actual_area_count = sum(len(item.get("control_areas", [])) for item in manifests)
        if expected_count != len(manifests) or expected_area_count != actual_area_count:
            raise ValueError("SERVER_DOMAIN_REGISTRY_COVERAGE_COUNT_MISMATCH")
        return manifests

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        """Return validated domain manifests, matching the Google Core manager API."""
        return self.list_domains()

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        key = str(domain_id).strip().upper()
        for domain in self.list_domains():
            if domain["domain_id"] == key:
                return domain
        return None

    def list_providers(self) -> list[dict[str, Any]]:
        return get_provider_catalog()

    def get_provider(self, provider_id: str) -> dict[str, Any] | None:
        from .provider_catalog import get_provider
        return get_provider(provider_id)

    def list_workloads(self) -> list[dict[str, Any]]:
        return get_workload_domain_catalog().get("domains", [])

    def get_workload(self, domain_id: str) -> dict[str, Any] | None:
        key = str(domain_id).strip().upper()
        return next((item for item in self.list_workloads()
                     if item.get("domain_id") == key), None)

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True,
            "provider_dependencies": [
                {
                    "provider_id": item["provider_id"],
                    "relationship": "PROVIDER_METADATA_NAMESPACE",
                    "remote_connection_verified": False,
                }
                for item in self.list_providers()
            ],
            "domain_dependencies": [
                {
                    "domain_id": item["domain_id"],
                    "relationship": "SERVER_CORE_CONTROL_DOMAIN",
                    "control_area_count": len(item.get("control_areas", [])),
                }
                for item in self.list_domains()
            ],
            "remote_operations_enabled": False,
        }

    def validate_providers(self) -> dict[str, Any]:
        providers = get_provider_catalog()
        seen: set[str] = set()
        for provider in providers:
            provider_id = provider.get("provider_id", "")
            folder = provider.get("folder", "")
            if not provider_id or provider_id in seen:
                raise ValueError(f"SERVER_PROVIDER_ID_MISSING_OR_DUPLICATE: {provider_id}")
            seen.add(provider_id)
            if not folder or not (ROOT / folder).is_dir():
                raise FileNotFoundError(f"SERVER_PROVIDER_DIRECTORY_MISSING: {folder}")
            manifest = _load_json(ROOT / folder / "provider_manifest.json")
            if manifest.get("provider_id") != provider_id:
                raise ValueError(f"SERVER_PROVIDER_MANIFEST_ID_MISMATCH: {provider_id}")
            if manifest.get("parent_id") != "GLOBAL-SERVER-CORE-ECOSYSTEM":
                raise ValueError(f"SERVER_PROVIDER_MANIFEST_PARENT_MISMATCH: {provider_id}")
            if manifest.get("status") != "CORE_CATALOG_ONLY":
                raise ValueError(f"SERVER_PROVIDER_STATUS_INVALID: {provider_id}")
            if (
                manifest.get("live_connection_verified") is not False
                or manifest.get("remote_operations_enabled") is not False
                or manifest.get("api_calls_performed") != 0
                or manifest.get("credential_storage") != "EXTERNAL_SECRET_STORE_ONLY"
            ):
                raise ValueError(f"SERVER_PROVIDER_OPERATIONAL_BOUNDARY_INVALID: {provider_id}")
        catalog_ids = {item["provider_id"] for item in providers}
        expected_ids = {
            "ABELOHOST", "AWS", "CLOUDFLARE", "DIGITALOCEAN",
            "GOOGLE", "MICROSOFT", "VICETEMPLE",
        }
        if catalog_ids != expected_ids:
            raise ValueError("SERVER_PROVIDER_CATALOG_COVERAGE_MISMATCH")
        return {"success": True, "provider_count": len(providers)}

    def validate_workload_profiles(self) -> dict[str, Any]:
        workload_catalog = get_workload_domain_catalog()
        domains = workload_catalog.get("domains", [])
        seen: set[str] = set()
        for item in domains:
            domain_id = item.get("domain_id", "")
            folder = domain_id.lower() + "_server_workload_profile"
            manifest_path = ROOT / folder / "workload_manifest.json"
            if not domain_id or domain_id in seen:
                raise ValueError(f"SERVER_WORKLOAD_ID_MISSING_OR_DUPLICATE: {domain_id}")
            seen.add(domain_id)
            if not manifest_path.is_file():
                raise FileNotFoundError(f"SERVER_WORKLOAD_MANIFEST_MISSING: {domain_id}")
            if not (ROOT / folder / "__init__.py").is_file():
                raise FileNotFoundError(f"SERVER_WORKLOAD_PACKAGE_INIT_MISSING: {domain_id}")
            manifest = _load_json(manifest_path)
            if manifest.get("domain_id") != domain_id:
                raise ValueError(f"SERVER_WORKLOAD_MANIFEST_ID_MISMATCH: {domain_id}")
            if manifest.get("profile_id") != f"SERVER-WORKLOAD-{domain_id}":
                raise ValueError(f"SERVER_WORKLOAD_PROFILE_ID_INVALID: {domain_id}")
            if manifest.get("scope") != "SERVER_REQUIREMENTS_METADATA_ONLY":
                raise ValueError(f"SERVER_WORKLOAD_SCOPE_INVALID: {domain_id}")
            if manifest.get("operational_status") != "NON_EXECUTING_PROFILE":
                raise ValueError(f"SERVER_WORKLOAD_OPERATIONAL_BOUNDARY_INVALID: {domain_id}")
            tiers = manifest.get("service_tiers", [])
            if tiers != ["NORMAL", "BASIC", "STANDARD", "PREMIUM",
                         "PROFESSIONAL", "ENTERPRISE", "SUPREME"]:
                raise ValueError(f"SERVER_WORKLOAD_SERVICE_TIERS_INVALID: {domain_id}")
            expected_areas = item.get("workload_areas", [])
            actual_areas = manifest.get("workload_areas", [])
            area_ids = [area.get("area_id") for area in actual_areas]
            if (
                len(expected_areas) != 5
                or len(actual_areas) != 5
                or manifest.get("workload_area_count") != 5
                or any(not area_id for area_id in area_ids)
                or len(area_ids) != len(set(area_ids))
                or any(not area.get("name") or not area.get("scope") for area in actual_areas)
            ):
                raise ValueError(f"SERVER_WORKLOAD_AREA_COUNT_OR_SCHEMA_INVALID: {domain_id}")
            if expected_areas != actual_areas:
                raise ValueError(f"SERVER_WORKLOAD_CATALOG_MANIFEST_MISMATCH: {domain_id}")
        return {
            "success": True,
            "workload_profile_count": len(domains),
            "workload_area_count": sum(len(x.get("workload_areas", [])) for x in domains),
        }

    def validate_scope_catalogs(self) -> dict[str, Any]:
        tiers = get_service_tier_catalog()
        expected = ["NORMAL", "BASIC", "STANDARD", "PREMIUM",
                    "PROFESSIONAL", "ENTERPRISE", "SUPREME"]
        actual = [item.get("tier_id") for item in tiers.get("tiers", [])]
        if actual != expected or tiers.get("tier_order") != expected:
            raise ValueError("SERVER_SERVICE_TIER_ORDER_INVALID")
        workload = self.validate_workload_profiles()
        geography = get_geographic_scope_catalog()
        if (geography.get("coverage_model") != "INDIA_FIRST_GLOBAL_EXTENSIBLE"
                or geography.get("india", {}).get("country_code") != "IN"):
            raise ValueError("SERVER_GEOGRAPHIC_SCOPE_INVALID")
        return {
            "success": True,
            "service_tier_count": len(actual),
            "workload_profile_count": workload["workload_profile_count"],
            "workload_area_count": workload["workload_area_count"],
            "geography_model": geography["coverage_model"],
        }

    def geography(self) -> dict[str, Any]:
        return get_geographic_scope_catalog()

    def service_tiers(self) -> list[dict[str, Any]]:
        return get_service_tier_catalog().get("tiers", [])

    def master_catalog_alignment(self) -> dict[str, Any]:
        return validate_master_alignment()

    def status(self) -> dict[str, Any]:
        registry = load_domain_registry()
        provider_validation = self.validate_providers()
        providers = get_provider_catalog()
        workload_validation = self.validate_workload_profiles()
        scope_validation = self.validate_scope_catalogs()
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
            "provider_validation": provider_validation,
            "core_domain_count": len(registry["domains"]),
            "domain_manifest_count": len(domains),
            "control_area_count": sum(len(x.get("control_areas", [])) for x in domains),
            "workload_profile_count": len(workloads),
            "workload_area_count": workload_validation["workload_area_count"],
            "workload_profile_validation": workload_validation,
            "scope_validation": scope_validation,
            "service_tier_count": len(tiers),
            "master_catalog_alignment": alignment,
            "live_provider_connections_verified": False,
            "remote_operations_enabled": False,
            "api_calls_performed": 0,
            "registry_persistence": "PROCESS_LOCAL_ONLY",
            "production_readiness_claimed": False,
            "health": "HEALTHY",
            "dependency_map_available": True,
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
