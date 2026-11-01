"""Read-only, source-aware registry service for the global Company API."""

import json
import string
from pathlib import Path
from typing import Any, Dict, List, Optional

PACKAGE_DIR = Path(__file__).resolve().parent
REGISTRY_PATH = PACKAGE_DIR / "data" / "company_registry.json"
ALLOWED_VERIFICATION_STATUSES = {
    "unverified", "source_checked", "registry_verified", "identity_verified", "suspended"
}


def load_company_registry() -> List[Dict[str, Any]]:
    """Load and validate normalized records from the local JSON registry."""
    if not REGISTRY_PATH.exists():
        return []
    with REGISTRY_PATH.open("r", encoding="utf-8") as registry_file:
        payload = json.load(registry_file)
    if not isinstance(payload, dict):
        raise ValueError("Company registry root must be an object")
    records = payload.get("records", [])
    if not isinstance(records, list):
        raise ValueError("Company registry 'records' must be a list")

    seen_ids = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"Company registry record {index} must be an object")
        company_id = str(record.get("company_id", "")).strip()
        name = str(record.get("name", "")).strip()
        entity_type = str(record.get("entity_type", "")).strip()
        if not company_id or not name or not entity_type:
            raise ValueError(f"Company registry record {index} requires company_id, name, and entity_type")
        if company_id in seen_ids:
            raise ValueError(f"Duplicate company_id: {company_id}")
        seen_ids.add(company_id)
        status = str(record.get("verification_status", "unverified")).casefold()
        if status not in ALLOWED_VERIFICATION_STATUSES:
            raise ValueError(f"Unsupported verification_status for {company_id}: {status}")
        sources = record.get("source_urls", [])
        if not isinstance(sources, list) or any(not isinstance(url, str) for url in sources):
            raise ValueError(f"source_urls for {company_id} must be a list of strings")
        if status in {"source_checked", "registry_verified", "identity_verified"} and not sources:
            raise ValueError(f"Verified record {company_id} must include source_urls")
    return records


def search_companies(
    q: Optional[str] = None,
    country: Optional[str] = None,
    industry: Optional[str] = None,
    entity_type: Optional[str] = None,
    verification_status: Optional[str] = None,
    letter: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
) -> Dict[str, Any]:
    """Filter, alphabetize, and paginate company/business records."""
    records = load_company_registry()
    query = q.casefold().strip() if q else None
    letter_filter = letter.casefold() if letter else None
    filtered = []

    for record in records:
        name = str(record.get("name", "")).strip()
        searchable = " ".join(
            [name]
            + [str(value) for value in record.get("aliases", [])]
            + [str(record.get("description", ""))]
        ).casefold()
        if query and query not in searchable:
            continue
        if letter_filter and not name.casefold().startswith(letter_filter):
            continue
        if country and str(record.get("country_code", "")).casefold() != country.casefold():
            continue
        if industry and industry.casefold() not in [
            str(value).casefold() for value in record.get("industries", [])
        ]:
            continue
        if entity_type and str(record.get("entity_type", "")).casefold() != entity_type.casefold():
            continue
        if verification_status and str(record.get("verification_status", "unverified")).casefold() != verification_status.casefold():
            continue
        filtered.append(record)

    filtered.sort(key=lambda item: (str(item.get("name", "")).casefold(), str(item.get("company_id", ""))))
    return {
        "total": len(filtered),
        "limit": limit,
        "offset": offset,
        "items": filtered[offset : offset + limit],
    }


def get_company(company_id: str) -> Optional[Dict[str, Any]]:
    """Return one record by its stable company_id."""
    for record in load_company_registry():
        if record.get("company_id") == company_id:
            return record
    return None


def get_company_alphabet() -> Dict[str, Any]:
    """Return A-Z company counts based on the first letter of each name."""
    counts = {letter: 0 for letter in string.ascii_uppercase}
    for record in load_company_registry():
        first = str(record.get("name", "")).strip()[:1].upper()
        if first in counts:
            counts[first] += 1
    return {"total": sum(counts.values()), "letters": counts}


def get_api_status() -> Dict[str, Any]:
    """Describe API readiness without implying that the directory is populated."""
    return {
        "ecosystem": "GLOBAL COMPANY AND COMPANIES API",
        "status": "available",
        "company_api": "available",
        "companies_api": "available",
        "registry_records": len(load_company_registry()),
        "source_count": len(load_country_sources()),
        "source_countries": sorted({item["country_code"] for item in load_country_sources()}),
        "registry_mode": "local_json_read_only",
        "source_mode": "official_source_directory_only",
        "note": "A-Z search and source provenance checks are enabled. Source descriptors are not live connections; company records require sourced evidence before verification.",
    }



def load_country_sources() -> List[Dict[str, Any]]:
    """Load the curated official-source directory; this does not connect to providers."""
    source_path = PACKAGE_DIR / "data" / "country_sources.json"
    if not source_path.exists():
        return []
    with source_path.open("r", encoding="utf-8") as source_file:
        payload = json.load(source_file)
    if not isinstance(payload, dict) or not isinstance(payload.get("sources"), list):
        raise ValueError("Country source registry must contain a sources list")
    seen = set()
    for index, source in enumerate(payload["sources"]):
        if not isinstance(source, dict):
            raise ValueError(f"Country source {index} must be an object")
        source_id = str(source.get("source_id", "")).strip()
        country_code = str(source.get("country_code", "")).strip()
        if not source_id or not country_code:
            raise ValueError(f"Country source {index} requires source_id and country_code")
        if source_id in seen:
            raise ValueError(f"Duplicate source_id: {source_id}")
        seen.add(source_id)
        if len(country_code) != 2 or not country_code.isalpha() or country_code != country_code.upper():
            raise ValueError(f"Invalid ISO alpha-2 country_code for source {source_id}")
        if not source.get("source_url"):
            raise ValueError(f"Country source {source_id} requires source_url")
    return payload["sources"]


def list_country_sources(country_code: Optional[str] = None) -> Dict[str, Any]:
    """List registered official source endpoints, optionally filtered by country."""
    sources = load_country_sources()
    if country_code:
        code = country_code.upper()
        sources = [item for item in sources if item["country_code"] == code]
    sources.sort(key=lambda item: (item["country_name"].casefold(), item["name"].casefold()))
    countries = sorted({item["country_code"] for item in sources})
    return {
        "total": len(sources),
        "country_count": len(countries),
        "countries": countries,
        "items": sources,
        "registry_status": "source_directory_only",
    }


def get_country_source(source_id: str) -> Optional[Dict[str, Any]]:
    """Get one official source descriptor by its stable source_id."""
    return next((item for item in load_country_sources() if item["source_id"] == source_id), None)
