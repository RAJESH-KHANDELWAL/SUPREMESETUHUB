"""Social platform domain taxonomy and coverage summary."""
from __future__ import annotations
from collections import Counter
from typing import Any
from .platform_catalog import list_platforms

def list_domain_inventory() -> list[dict[str, Any]]:
    counts = Counter(item["category"] for item in list_platforms())
    return [{"domain_id": key, "name": key.replace("_", " ").title(), "platform_count": counts[key]} for key in sorted(counts)]

def domain_summary() -> dict[str, Any]:
    platforms = list_platforms()
    domains = list_domain_inventory()
    return {
        "success": True,
        "domain_count": len(domains),
        "domains": domains,
        "platform_package_count": len(platforms),
        "provider_count": sum(item["package_type"] == "PLATFORM" for item in platforms),
        "family_count": sum(item["package_type"] == "PLATFORM_FAMILY" for item in platforms),
        "age_restricted_platform_count": sum(item["category"].startswith("adult_") or item["id"] == "adult_community_platforms" for item in platforms),
        "geographic_scope": "BHARAT_FIRST_GLOBAL_EXTENSIBLE",
        "live_connections_verified": 0,
        "note": "Taxonomy and access labels are discovery metadata, not proof of API availability, approval or a live connection.",
    }
