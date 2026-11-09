"""Read-only adapter to the canonical Bada Business resource catalog.

No provider URLs or program records are duplicated in this AI package.
"""
from __future__ import annotations
from typing import Any


def load_provider_resources() -> dict[str, Any]:
    """Load canonical resources from the product/resource ownership layer."""
    try:
        from backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog import get_catalog
    except ImportError as exc:
        raise RuntimeError("BADA_BUSINESS_RESOURCE_CATALOG_UNAVAILABLE") from exc

    catalog = get_catalog()
    if not isinstance(catalog, dict):
        raise RuntimeError("BADA_BUSINESS_RESOURCE_CATALOG_INVALID")
    return catalog


def resource_summary(catalog: dict[str, Any] | None = None) -> dict[str, Any]:
    """Return safe resource counts without copying provider records into AI storage."""
    data = catalog if catalog is not None else load_provider_resources()
    links = data.get("links", [])
    programs = data.get("programs", {})
    return {
        "ecosystem_id": data.get("ecosystem_id", "BADA_BUSINESS_ECOSYSTEM"),
        "resource_status": data.get("status", "UNKNOWN"),
        "link_count": len(links) if isinstance(links, list) else 0,
        "program_count": len(programs) if isinstance(programs, dict) else 0,
        "resource_catalog_available": True,
    }
