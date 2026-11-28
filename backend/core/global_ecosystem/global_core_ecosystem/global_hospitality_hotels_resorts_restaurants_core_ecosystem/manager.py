"""Entry point for the Global Hospitality Core Ecosystem.

Keeps domain taxonomy and geographic reference contracts in the CORE layer.
Operational services and commercial workflows live in the paired Bada Business
service-work-business ecosystem.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

CORE_ROOT = Path(__file__).resolve().parent
GEOGRAPHY_ROOT = CORE_ROOT / "global"
INDIA_ROOT = CORE_ROOT / "india"
CATEGORY_ROOT = CORE_ROOT / "categories"


def ecosystem_manifest() -> dict[str, Any]:
    """Return stable paths and coverage domains for discovery and validation."""
    return {
        "name": "global_hospitality_hotels_resorts_restaurants_core_ecosystem",
        "coverage": ["global", "bharat", "states", "union_territories", "districts",
                     "sub_districts", "cities", "towns", "villages", "localities", "streets"],
        "hospitality_categories": [
            "hotels", "resorts", "restaurants", "cafes", "dhabas", "homestays",
            "hostels", "serviced_apartments", "banquet_venues", "convention_facilities"
        ],
        "paths": {
            "global": str(GEOGRAPHY_ROOT),
            "india": str(INDIA_ROOT),
            "categories": str(CATEGORY_ROOT),
        },
        "source_policy": "verified_or_authoritative_sources_only",
    }


def validate_geography_record(record: dict[str, Any]) -> list[str]:
    """Validate minimum provenance and hierarchy fields for a geography record."""
    required = ("id", "name", "level", "country_code", "source", "verification_status")
    errors = [f"missing required field: {field}" for field in required if not record.get(field)]
    allowed_levels = {
        "country", "state", "union_territory", "province", "region", "district",
        "county", "sub_district", "tehsil", "block", "city", "town", "village",
        "gram_panchayat", "ward", "locality", "street"
    }
    if record.get("level") and record["level"] not in allowed_levels:
        errors.append("unsupported geography level")
    return errors
