"""Read-only, source-aware global organization directory."""
import json
from pathlib import Path
from typing import Any
from .catalog import ORGANIZATION_DOMAINS, ORGANIZATION_TYPES, VERIFICATION_STATES

PACKAGE_DIR = Path(__file__).resolve().parent
REGISTRY_PATH = PACKAGE_DIR / "data" / "organization_registry.json"
DOMAIN_IDS = {item["domain_id"] for item in ORGANIZATION_DOMAINS}
TYPE_IDS = {item["type_id"] for item in ORGANIZATION_TYPES}

def load_organization_registry() -> list[dict[str, Any]]:
    """Load canonical records. Missing registry means an empty directory."""
    if not REGISTRY_PATH.exists():
        return []
    payload = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("records", []), list):
        raise ValueError("Organization registry must contain a records list")
    records, seen = payload.get("records", []), set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"Organization record {index} must be an object")
        oid, name = str(record.get("organization_id", "")).strip(), str(record.get("name", "")).strip()
        if not oid or not name:
            raise ValueError(f"Organization record {index} requires organization_id and name")
        if oid in seen:
            raise ValueError(f"Duplicate organization_id: {oid}")
        seen.add(oid)
        if record.get("organization_type") not in TYPE_IDS:
            raise ValueError(f"Unsupported organization_type for {oid}")
        if record.get("domain_id") not in DOMAIN_IDS:
            raise ValueError(f"Unsupported domain_id for {oid}")
        status = record.get("verification_status", "unverified")
        if status not in VERIFICATION_STATES:
            raise ValueError(f"Unsupported verification status for {oid}")
        if status in {"source_checked", "identity_verified", "registry_verified"} and not record.get("source_urls"):
            raise ValueError(f"Verified organization {oid} requires source_urls")
        if not isinstance(record.get("country_codes", []), list) or not isinstance(record.get("source_urls", []), list):
            raise ValueError(f"country_codes and source_urls for {oid} must be lists")
    return records

def get_ecosystem_status() -> dict[str, Any]:
    records = load_organization_registry()
    return {"ecosystem":"GLOBAL ORGANIZATIONS API ECOSYSTEM","status":"ready_with_records" if records else "registry_empty","organization_count":len(records),"domain_count":len(ORGANIZATION_DOMAINS),"organization_type_count":len(ORGANIZATION_TYPES),"registry_mode":"local_json_read_only","taxonomy_mode":"curated_metadata","live_external_connections":False,"note":"Organization identity is distinct from Company and Platform identity. Taxonomy does not imply legal verification or complete worldwide coverage."}

def search_organizations(q: str | None = None, domain: str | None = None, country: str | None = None, organization_type: str | None = None, verification_status: str | None = None, limit: int = 50, offset: int = 0) -> dict[str, Any]:
    if limit < 1 or limit > 200 or offset < 0:
        raise ValueError("limit must be 1..200 and offset non-negative")
    query, results = (q.casefold().strip() if q else None), []
    for record in load_organization_registry():
        searchable = " ".join([str(record.get("name","")), str(record.get("description","")), *[str(x) for x in record.get("aliases",[])] ]).casefold()
        if query and query not in searchable: continue
        if domain and str(record.get("domain_id","")).casefold() != domain.casefold(): continue
        if country and country.upper() not in [str(x).upper() for x in record.get("country_codes",[])]: continue
        if organization_type and str(record.get("organization_type","")).casefold() != organization_type.casefold(): continue
        if verification_status and str(record.get("verification_status","unverified")).casefold() != verification_status.casefold(): continue
        results.append(record)
    results.sort(key=lambda x:(str(x.get("name","")).casefold(),str(x.get("organization_id",""))))
    return {"total":len(results),"limit":limit,"offset":offset,"items":results[offset:offset+limit]}

def get_organization(organization_id: str) -> dict[str, Any] | None:
    return next((item for item in load_organization_registry() if item["organization_id"] == organization_id), None)
