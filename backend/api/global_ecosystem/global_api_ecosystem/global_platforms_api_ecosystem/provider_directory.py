"""Source-aware metadata directory for provider-specific Platform packages.

Entries describe package ownership and classification only. They do not claim
that a provider API is available, authenticated, or connected.
"""
from __future__ import annotations

from importlib import import_module
from typing import Any

PROVIDERS = (
    ("apple", "Apple", "apple_platforms_api_ecosystem", False),
    ("aws", "Amazon Web Services", "aws_platforms_api_ecosystem", False),
    ("google", "Google", "google_platforms_api_ecosystem", False),
    ("microsoft", "Microsoft", "microsoft_platforms_api_ecosystem", False),
    ("bangbros", "BangBros", "bangbros_platforms_api_ecosystem", True),
    ("brazzers", "Brazzers", "brazzers_platforms_api_ecosystem", True),
    ("clips4sale", "Clips4Sale", "clips4sale_platforms_api_ecosystem", True),
    ("evilangel", "Evil Angel", "evilangel_platforms_api_ecosystem", True),
    ("fansly", "Fansly", "fansly_platforms_api_ecosystem", True),
    ("faphouse", "FapHouse", "faphouse_platforms_api_ecosystem", True),
    ("loyalfans", "LoyalFans", "loyalfans_platforms_api_ecosystem", True),
    ("manyvids", "ManyVids", "manyvids_platforms_api_ecosystem", True),
    ("naughtyamerica", "Naughty America", "naughtyamerica_platforms_api_ecosystem", True),
    ("onlyfans", "OnlyFans", "onlyfans_platforms_api_ecosystem", True),
    ("pornhub", "Pornhub", "pornhub_platforms_api_ecosystem", True),
    ("realitykings", "Reality Kings", "realitykings_platforms_api_ecosystem", True),
    ("xhamster", "xHamster", "xhamster_platforms_api_ecosystem", True),
    ("xvideos", "XVideos", "xvideos_platforms_api_ecosystem", True),
)


def _provider_record(entry: tuple[str, str, str, bool]) -> dict[str, Any]:
    provider_id, fallback_name, folder, adult_only = entry
    module = import_module(f".{folder}.{folder}", package=__package__)
    return {
        "provider_id": provider_id,
        "name": fallback_name,
        "provider_name": module.PROVIDER_NAME,
        "category_id": module.CATEGORY_ID,
        "category_name": module.CATEGORY_NAME,
        "provider_catalog_path": module.PROVIDER_CATALOG_PATH,
        "category_catalog_path": module.CATEGORY_CATALOG_PATH,
        "implementation_status": module.IMPLEMENTATION_STATUS,
        "api_documentation_verified": bool(module.API_DOCUMENTATION_VERIFIED),
        "live_connection_verified": bool(module.LIVE_CONNECTION_VERIFIED),
        "adult_only": adult_only,
        "minimum_age": 18 if adult_only else None,
        "package_status": "metadata_only",
    }


def list_platform_providers(include_adult: bool = False) -> list[dict[str, Any]]:
    entries = [entry for entry in PROVIDERS if include_adult or not entry[3]]
    records = [_provider_record(entry) for entry in entries]
    return sorted(records, key=lambda item: item["provider_id"])


def get_platform_provider(provider_id: str, include_adult: bool = False) -> dict[str, Any] | None:
    wanted = (provider_id or "").strip().casefold()
    entry = next((item for item in PROVIDERS if item[0] == wanted), None)
    if entry is None or (entry[3] and not include_adult):
        return None
    return _provider_record(entry)


def get_provider_directory_status() -> dict[str, Any]:
    return {
        "provider_count": len(PROVIDERS),
        "adult_provider_count": sum(1 for item in PROVIDERS if item[3]),
        "non_adult_provider_count": sum(1 for item in PROVIDERS if not item[3]),
        "implementation_status": "metadata_only",
        "live_connections": 0,
    }
