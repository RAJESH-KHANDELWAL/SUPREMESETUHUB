"""Connection adapter to the canonical Global Bada Business ecosystem.

Reads the existing resource package directly. It does not duplicate program
records, submit registrations, process payments, or claim a live provider API.
"""
from __future__ import annotations
from typing import Any

from backend.global_ecosystem.global_bada_business_ecosystem import (
    ECOSYSTEM as BADA_BUSINESS_ECOSYSTEM,
    get_catalog as get_bada_business_catalog,
    list_courses,
    list_events,
    list_programs,
)
from backend.global_ecosystem.global_bada_business_ecosystem.global_network_marketing_direct_selling_business_ecosystem.catalog import (
    list_business_ecosystems as list_network_marketing_ecosystems,
)

def get_bada_business_connection() -> dict[str, Any]:
    """Return a live code-level package connection and safe resource counts."""
    provider_catalog = get_bada_business_catalog()
    network_children = list_network_marketing_ecosystems()
    return {
        "parent_ecosystem_id": "global_business_ecosystem",
        "child_ecosystem_id": "global_bada_business_ecosystem",
        "child_ecosystem": dict(BADA_BUSINESS_ECOSYSTEM),
        "connection_type": "DIRECT_PYTHON_PACKAGE_ADAPTER",
        "code_connection": True,
        "resource_catalog_available": bool(provider_catalog.get("success")),
        "program_count": len(list_programs()),
        "course_count": len(list_courses()),
        "event_count": len(list_events()),
        "network_marketing_child_count": len(network_children),
        "provider_catalog_status": provider_catalog.get("status", "UNKNOWN"),
        "official_public_api_verified": bool(provider_catalog.get("official_public_api_verified", False)),
        "live_provider_connection_verified": bool(provider_catalog.get("live_connection_verified", False)),
        "canonical_resource_package": "backend.global_ecosystem.global_bada_business_ecosystem",
        "network_marketing_package": (
            "backend.global_ecosystem.global_bada_business_ecosystem."
            "global_network_marketing_direct_selling_business_ecosystem"
        ),
    }

__all__ = ["get_bada_business_connection"]
