"""Bharat-to-global regional profile catalogue; no live jurisdictional advice."""
from __future__ import annotations

_PROFILES = {
    "india": {"scope": "national", "subdivisions": ("states", "union_territories", "districts", "cities", "rural_areas")},
    "south_asia": {"scope": "regional", "subdivisions": ("country", "province", "district", "municipality")},
    "apac": {"scope": "regional", "subdivisions": ("country", "state_or_province", "local_authority")},
    "middle_east": {"scope": "regional", "subdivisions": ("country", "governorate_or_region", "local_authority")},
    "africa": {"scope": "regional", "subdivisions": ("country", "province_or_region", "district")},
    "europe": {"scope": "regional", "subdivisions": ("country", "region", "municipality")},
    "north_america": {"scope": "regional", "subdivisions": ("country", "state_or_province", "county_or_municipality")},
    "latin_america": {"scope": "regional", "subdivisions": ("country", "state_or_department", "municipality")},
    "oceania": {"scope": "regional", "subdivisions": ("country", "state_or_territory", "local_council")},
    "global": {"scope": "cross_border", "subdivisions": ("country", "jurisdiction", "local_authority")},
}

def regional_profiles() -> dict[str, dict[str, object]]:
    return {key: {**value, "subdivisions": tuple(value["subdivisions"])} for key, value in _PROFILES.items()}

def resolve_region(region: str) -> dict[str, object] | None:
    key = str(region or "").strip().casefold().replace("-", "_").replace(" ", "_")
    value = _PROFILES.get(key)
    return None if value is None else {**value, "region": key, "requires_local_legal_review": True}
