"""Canonical 16-domain Server Core inventory and workload coverage."""
from __future__ import annotations
from collections import Counter
from typing import Any
from .domain_registry import load_domain_registry
from .scope_catalog import get_workload_domain_catalog

def list_server_core_domain_inventory() -> list[dict[str, Any]]:
    registry = load_domain_registry()
    return [dict(item) for item in registry.get("domains", [])]

def server_core_domain_summary() -> dict[str, Any]:
    domains = list_server_core_domain_inventory()
    workload = get_workload_domain_catalog().get("domains", [])
    return {
        "success": True,
        "domain_count": len(domains),
        "domains": domains,
        "workload_domain_count": len(workload),
        "workload_profile_count": len(workload),
        "geographic_scope": "BHARAT_FIRST_GLOBAL_EXTENSIBLE",
        "service_tier_count": 7,
        "live_connections_verified": 0,
        "note": "Domain and workload assignments are metadata classifications, not deployed services or provider connectivity."
    }
