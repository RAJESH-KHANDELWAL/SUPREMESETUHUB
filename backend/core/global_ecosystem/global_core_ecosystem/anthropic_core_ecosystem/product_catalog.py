"""Unified inventory of the registered Anthropic Core product families.

This is a provider Core catalog view, not proof of API availability or live
connectivity. Product identities are sourced from catalog.py only.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from .catalog import list_anthropic_core_modules


def list_anthropic_offerings() -> list[dict[str, Any]]:
    """Return registered Anthropic product families with Core routing metadata."""
    results: list[dict[str, Any]] = []
    for module in list_anthropic_core_modules():
        item = deepcopy(module)
        item["core_family_id"] = item["ecosystem_id"]
        item["core_mapping_status"] = "MAPPED_TO_CORE_FAMILY"
        item["api_available"] = None  # Must be verified by the API layer.
        results.append(item)
    return results


def anthropic_offerings_summary() -> dict[str, Any]:
    offerings = list_anthropic_offerings()
    return {
        "success": True,
        "offering_count": len(offerings),
        "mapped_count": len(offerings),
        "unmapped_count": 0,
        "api_availability_verified_count": 0,
        "live_connections_verified": 0,
        "offerings": offerings,
        "note": "Core registration is inventory metadata, not API availability, entitlement, authorization or live connectivity.",
    }
