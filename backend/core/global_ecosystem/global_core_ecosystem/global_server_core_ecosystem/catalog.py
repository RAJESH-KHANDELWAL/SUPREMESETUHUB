"""Canonical provider-neutral SERVER CORE catalog."""
from __future__ import annotations

from copy import deepcopy

from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME, CAPABILITIES
from .domain_registry import load_domain_registry
from .provider_catalog import get_provider_catalog, provider_summary
from .scope_catalog import get_scope_catalog


def get_catalog():
    """Return providers, CORE domains and Bharat-to-global scope metadata."""
    scope = get_scope_catalog()
    registry = load_domain_registry()
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "layer": "CORE",
        "status": "CORE_CATALOG_AND_WORKLOAD_PROFILES",
        "capabilities": list(CAPABILITIES),
        "providers": get_provider_catalog(),
        **provider_summary(),
        "core_domains": registry["domains"],
        "core_domain_count": len(registry["domains"]),
        "control_area_count": registry.get("control_area_count", 0),
        "service_tiers": scope["service_tiers"]["tiers"],
        "geographic_scope": scope["geographic_scope"],
        "workload_domains": scope["workload_domains"]["domains"],
        "workload_domain_count": len(scope["workload_domains"]["domains"]),
        "adult_workload_policy": scope["workload_domains"]["adult_workload_policy"],
        "master_catalog_source": registry["master_catalog_source"],
        "master_catalog_access_mode": registry["master_catalog_access_mode"],
        "remote_operations_enabled": False,
        "api_calls_performed": 0,
        "registry_persistence": "PROCESS_LOCAL_ONLY",
    }


def get_server_core_catalog():
    return deepcopy(get_catalog())
