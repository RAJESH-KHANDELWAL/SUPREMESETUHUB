"""Catalog service for GLOBAL ADULT INDUSTRY ECOSYSTEM."""
from __future__ import annotations

from typing import Any

from backend.api.global_api_ecosystem_catalog import list_provider_ecosystems


ADULT_INDUSTRY_PROVIDER_IDS = {
    "abelohost", "vicetemple", "faphouse", "pornhub", "naughtyamerica",
}


def list_adult_industry_providers() -> list[dict[str, Any]]:
    """Return adult-industry provider records; catalog membership is not connectivity."""
    return [
        record
        for record in list_provider_ecosystems("ADULT_INDUSTRY")
        if record["provider_id"] in ADULT_INDUSTRY_PROVIDER_IDS
    ]


def get_adult_industry_status() -> dict[str, Any]:
    providers = list_adult_industry_providers()
    return {
        "success": True,
        "system": "GLOBAL ADULT INDUSTRY ECOSYSTEM",
        "provider_count": len(providers),
        "live_connections_verified": sum(
            1 for provider in providers if provider.get("live_connection_verified") is True
        ),
        "catalog_only_is_not_connected": True,
    }
