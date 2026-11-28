"""Adobe Core domain inventory and summaries derived from the canonical provider catalog."""
from __future__ import annotations
from typing import Any
from .catalog import get_adobe_core_catalog

PROVIDER_GOVERNANCE = {
    "domain_id": "PROVIDER_GOVERNANCE",
    "domain_key": "provider_governance",
    "name": "Adobe Provider Governance",
    "purpose": "Provider identity, product registration, catalog lifecycle, policy and readiness.",
}

def list_adobe_domain_inventory() -> list[dict[str, Any]]:
    catalog = get_adobe_core_catalog()
    domains = [dict(PROVIDER_GOVERNANCE)]
    for item in catalog.get("children", []):
        domains.append({
            "domain_id": item["product_key"].upper(),
            "domain_key": item["product_key"],
            "name": item["name"],
            "purpose": item.get("description", ""),
            "ecosystem_id": item["ecosystem_id"],
            "core_module": item["core_module"],
            "api_catalog_refs": item.get("api_catalog_refs", []),
            "api_mapping_status": item.get("api_mapping_status", "UNMAPPED"),
            "status": item.get("status", "UNKNOWN"),
            "enabled": bool(item.get("enabled", True)),
        })
    return domains

def adobe_domain_summary() -> dict[str, Any]:
    inventory = list_adobe_domain_inventory()
    return {
        "success": True,
        "ecosystem_id": "ADOBE-CORE-ECOSYSTEM",
        "domain_count": len(inventory),
        "domains": inventory,
        "live_connections_verified": 0,
        "api_calls_performed": 0,
    }

__all__ = ["PROVIDER_GOVERNANCE", "list_adobe_domain_inventory", "adobe_domain_summary"]
