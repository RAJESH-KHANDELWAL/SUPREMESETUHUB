"""Read-only platform taxonomy and source-aware profile directory."""
import json
from pathlib import Path
from typing import Any, Optional

from .catalog import (
    BUSINESS_MODELS,
    OWNERSHIP_TYPES,
    PLATFORM_DOMAINS,
    PLATFORM_TYPES,
    VERIFICATION_STATES,
)

PACKAGE_DIR = Path(__file__).resolve().parent
REGISTRY_PATH = PACKAGE_DIR / "data" / "platform_registry.json"
DOMAIN_IDS = {item["domain_id"] for item in PLATFORM_DOMAINS}


def load_platform_registry() -> list[dict[str, Any]]:
    """Load platform profiles and enforce identity, classification and provenance."""
    if not REGISTRY_PATH.exists():
        return []
    with REGISTRY_PATH.open("r", encoding="utf-8") as stream:
        payload = json.load(stream)
    if not isinstance(payload, dict) or not isinstance(payload.get("records", []), list):
        raise ValueError("Platform registry must contain a records list")

    records = payload.get("records", [])
    seen: set[str] = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"Platform record {index} must be an object")
        platform_id = str(record.get("platform_id", "")).strip()
        name = str(record.get("name", "")).strip()
        if not platform_id or not name:
            raise ValueError(f"Platform record {index} requires platform_id and name")
        if platform_id in seen:
            raise ValueError(f"Duplicate platform_id: {platform_id}")
        seen.add(platform_id)

        domain_id = record.get("domain_id")
        if domain_id is not None and domain_id not in DOMAIN_IDS:
            raise ValueError(f"Unsupported domain_id for {platform_id}: {domain_id}")
        platform_type = record.get("platform_type")
        if platform_type is not None and platform_type not in PLATFORM_TYPES:
            raise ValueError(f"Unsupported platform_type for {platform_id}: {platform_type}")
        ownership_type = record.get("ownership_type")
        if ownership_type is not None and ownership_type not in OWNERSHIP_TYPES:
            raise ValueError(f"Unsupported ownership_type for {platform_id}: {ownership_type}")
        business_model = record.get("business_model")
        if business_model is not None and business_model not in BUSINESS_MODELS:
            raise ValueError(f"Unsupported business_model for {platform_id}: {business_model}")

        country_codes = record.get("country_codes", [])
        if not isinstance(country_codes, list) or any(
            not isinstance(code, str) or len(code) != 2 or not code.isalpha() or code != code.upper()
            for code in country_codes
        ):
            raise ValueError(f"country_codes for {platform_id} must be ISO alpha-2 codes")

        sources = record.get("source_urls", [])
        if not isinstance(sources, list) or any(not isinstance(url, str) or not url.strip() for url in sources):
            raise ValueError(f"source_urls for {platform_id} must be a list of non-empty strings")

        status = str(record.get("verification_status", "unverified")).casefold()
        if status not in VERIFICATION_STATES:
            raise ValueError(f"Unsupported verification status for {platform_id}")
        if status in {"source_checked", "identity_verified", "operator_verified"} and not sources:
            raise ValueError(f"Verified platform {platform_id} requires source_urls")

        adult_only = record.get("adult_only", False)
        if not isinstance(adult_only, bool):
            raise ValueError(f"adult_only for {platform_id} must be boolean")
        if adult_only:
            try:
                minimum_age = int(record.get("minimum_age", 0))
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Adult platform {platform_id} must require age 18 or above") from exc
            if minimum_age < 18:
                raise ValueError(f"Adult platform {platform_id} must require age 18 or above")
            if domain_id and domain_id != "adult_industry":
                raise ValueError(f"Adult platform {platform_id} must use the adult_industry domain")
    return records


def get_ecosystem_status() -> dict[str, Any]:
    records = load_platform_registry()
    return {
        "ecosystem": "GLOBAL PLATFORMS API ECOSYSTEM",
        "status": "ready_with_records" if records else "registry_empty",
        "profile_count": len(records),
        "domain_count": len(PLATFORM_DOMAINS),
        "platform_type_count": len(PLATFORM_TYPES),
        "registry_mode": "local_json_read_only",
        "taxonomy_mode": "curated_metadata",
        "live_external_connections": False,
        "verified_profile_count": sum(
            1 for item in records
            if item.get("verification_status", "unverified") in {"source_checked", "identity_verified", "operator_verified"}
        ),
        "note": "Directory records are unverified discovery metadata unless a record explicitly carries source-backed verification. Taxonomy availability does not imply live integrations or complete worldwide coverage.",
    }


def list_domains(include_adult: bool = False) -> list[dict[str, Any]]:
    return [domain for domain in PLATFORM_DOMAINS if include_adult or not domain.get("adult_only", False)]


def get_domain(domain_id: str) -> Optional[dict[str, Any]]:
    return next((domain for domain in PLATFORM_DOMAINS if domain["domain_id"] == domain_id), None)


def search_platforms(
    q: Optional[str] = None,
    domain: Optional[str] = None,
    country: Optional[str] = None,
    platform_type: Optional[str] = None,
    verification_status: Optional[str] = None,
    include_adult: bool = False,
    limit: int = 50,
    offset: int = 0,
) -> dict[str, Any]:
    """Search platform profiles using independent classification dimensions."""
    if limit < 1 or limit > 200 or offset < 0:
        raise ValueError("limit must be 1..200 and offset non-negative")
    if domain and domain not in DOMAIN_IDS:
        raise ValueError("Unknown platform domain")
    if platform_type and platform_type not in PLATFORM_TYPES:
        raise ValueError("Unsupported platform_type")
    if verification_status and verification_status not in VERIFICATION_STATES:
        raise ValueError("Unsupported verification_status")

    query = q.casefold().strip() if q else None
    results = []
    for record in load_platform_registry():
        if record.get("adult_only") and not include_adult:
            continue
        searchable = " ".join([
            str(record.get("name", "")),
            str(record.get("description", "")),
            *[str(alias) for alias in record.get("aliases", [])],
        ]).casefold()
        if query and query not in searchable:
            continue
        if domain and str(record.get("domain_id", "")).casefold() != domain.casefold():
            continue
        if country and country.upper() not in [str(code).upper() for code in record.get("country_codes", [])]:
            continue
        if platform_type and str(record.get("platform_type", "")).casefold() != platform_type.casefold():
            continue
        if verification_status and str(record.get("verification_status", "unverified")).casefold() != verification_status.casefold():
            continue
        results.append(record)

    results.sort(key=lambda item: (
        str(item.get("name", "")).casefold(),
        str(item.get("platform_id", "")),
    ))
    return {
        "total": len(results),
        "limit": limit,
        "offset": offset,
        "include_adult": include_adult,
        "items": results[offset:offset + limit],
    }


def get_platform(platform_id: str, include_adult: bool = False) -> Optional[dict[str, Any]]:
    record = next(
        (item for item in load_platform_registry() if item["platform_id"] == platform_id),
        None,
    )
    return None if record and record.get("adult_only") and not include_adult else record
