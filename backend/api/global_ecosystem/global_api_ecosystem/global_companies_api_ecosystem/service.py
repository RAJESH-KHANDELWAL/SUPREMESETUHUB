"""Read-only registry service for the global Company / Companies API.

The registry intentionally starts empty. Only sourced, reviewed records should
be added; this module never fabricates company profiles.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

PACKAGE_DIR = Path(__file__).resolve().parent
REGISTRY_PATH = PACKAGE_DIR / "data" / "company_registry.json"


def load_company_registry() -> List[Dict[str, Any]]:
    """Load normalized records from the package registry."""
    if not REGISTRY_PATH.exists():
        return []
    with REGISTRY_PATH.open("r", encoding="utf-8") as registry_file:
        payload = json.load(registry_file)
    records = payload.get("records", [])
    if not isinstance(records, list):
        raise ValueError("Company registry 'records' must be a list")
    return records


def search_companies(
    q: Optional[str] = None,
    country: Optional[str] = None,
    industry: Optional[str] = None,
    entity_type: Optional[str] = None,
    verification_status: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
) -> Dict[str, Any]:
    """Filter registry records and return a stable paginated response."""
    records = load_company_registry()
    query = q.casefold().strip() if q else None
    filtered = []

    for record in records:
        searchable = " ".join(
            [str(record.get("name", ""))]
            + [str(value) for value in record.get("aliases", [])]
            + [str(record.get("description", ""))]
        ).casefold()
        if query and query not in searchable:
            continue
        if country and str(record.get("country_code", "")).casefold() != country.casefold():
            continue
        if industry and industry.casefold() not in [
            str(value).casefold() for value in record.get("industries", [])
        ]:
            continue
        if entity_type and str(record.get("entity_type", "")).casefold() != entity_type.casefold():
            continue
        if verification_status and str(record.get("verification_status", "")).casefold() != verification_status.casefold():
            continue
        filtered.append(record)

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


def get_api_status() -> Dict[str, Any]:
    """Describe API readiness without implying that the directory is populated."""
    return {
        "ecosystem": "GLOBAL COMPANY AND COMPANIES API",
        "status": "available",
        "company_api": "available",
        "companies_api": "available",
        "registry_records": len(load_company_registry()),
        "registry_mode": "local_json_read_only",
        "note": "API is operational; directory records are added only after sourcing and verification.",
    }
