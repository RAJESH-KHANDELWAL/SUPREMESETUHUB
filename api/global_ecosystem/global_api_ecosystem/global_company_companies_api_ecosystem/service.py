"""Read-only, source-aware registry service for the global company ecosystem."""
import json
import string
from pathlib import Path
from typing import Any, Dict, List, Optional

PACKAGE_DIR = Path(__file__).resolve().parent
REGISTRY_PATH = PACKAGE_DIR / "data" / "company_registry.json"
ALLOWED_VERIFICATION_STATUSES = {"unverified", "source_checked", "registry_verified", "identity_verified", "suspended"}
ALLOWED_RECORD_TYPES = {"company", "enterprise", "corporate_group", "freelancer", "business"}
ENTITY_TYPE_GROUPS = {
    "company": {"registered_company", "public_company", "private_company", "limited_company", "corporation", "private_limited_company", "public_limited_company", "limited_liability_company", "government_enterprise", "state_owned_enterprise", "public_sector_organization", "nonprofit", "charity", "foundation", "cooperative", "partnership", "limited_liability_partnership", "holding_company", "subsidiary", "joint_venture", "branch_office", "multinational"},
    "enterprise": {"sole_proprietor", "micro_business", "small_business", "medium_business", "large_business", "large_enterprise", "startup", "scaleup", "franchise", "operating_enterprise", "micro_enterprise", "small_enterprise", "medium_enterprise"},
    "corporate_group": {"corporate_group", "holding_group", "parent_company_group", "subsidiary_group", "multinational_group", "conglomerate_group"},
    "freelancer": {"freelancer", "individual_service_provider", "self_employed", "independent_consultant", "independent_contractor", "gig_worker", "professional_practice"},
}

def infer_record_type(record: Dict[str, Any]) -> Optional[str]:
    explicit = str(record.get("record_type", "")).casefold().strip()
    if explicit == "business":
        return "enterprise"
    if explicit:
        return explicit
    entity = str(record.get("entity_type", "")).casefold().strip()
    for category, entity_types in ENTITY_TYPE_GROUPS.items():
        if entity in entity_types:
            return category
    return None

def load_company_registry() -> List[Dict[str, Any]]:
    """Load records and enforce stable identity, category and provenance rules."""
    if not REGISTRY_PATH.exists():
        return []
    with REGISTRY_PATH.open("r", encoding="utf-8") as f:
        payload = json.load(f)
    if not isinstance(payload, dict):
        raise ValueError("Company registry root must be an object")
    records = payload.get("records", [])
    if not isinstance(records, list):
        raise ValueError("Company registry 'records' must be a list")
    seen = set()
    for i, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"Company registry record {i} must be an object")
        record_id = str(record.get("company_id", "")).strip()
        name = str(record.get("name", "")).strip()
        entity = str(record.get("entity_type", "")).strip()
        if not record_id or not name or not entity:
            raise ValueError(f"Company registry record {i} requires company_id, name, and entity_type")
        if record_id in seen:
            raise ValueError(f"Duplicate company_id: {record_id}")
        seen.add(record_id)
        category = infer_record_type(record)
        if category not in ALLOWED_RECORD_TYPES:
            entity_type = str(record.get("entity_type", "")).strip()
            raise ValueError(
                f"Unsupported entity_type/record_type for {record_id}: "
                f"{entity_type or category or 'missing classification'}"
            )
        record["record_type"] = category
        status = str(record.get("verification_status", "unverified")).casefold()
        if status not in ALLOWED_VERIFICATION_STATUSES:
            raise ValueError(f"Unsupported verification_status for {record_id}: {status}")
        sources = record.get("source_urls", [])
        if not isinstance(sources, list) or any(
            not isinstance(url, str) or not url.strip()
            or not url.strip().startswith(("https://", "http://"))
            for url in sources
        ):
            raise ValueError(f"source_urls for {record_id} must be a list of absolute HTTP(S) URLs")
        if status in {"source_checked", "registry_verified", "identity_verified"} and not sources:
            raise ValueError(f"Verified record {record_id} must include source_urls")
    return records

def search_companies(q: Optional[str] = None, country: Optional[str] = None, industry: Optional[str] = None,
                     entity_type: Optional[str] = None, verification_status: Optional[str] = None,
                     letter: Optional[str] = None, limit: int = 50, offset: int = 0,
                     category: Optional[str] = None) -> Dict[str, Any]:
    """Search source-backed profiles with canonical Company, Enterprise and Corporate Group classes; retain legacy freelancer filtering for compatibility."""
    if limit < 1 or limit > 200 or offset < 0:
        raise ValueError("limit must be 1..200 and offset non-negative")
    if verification_status and verification_status.casefold() not in ALLOWED_VERIFICATION_STATUSES:
        raise ValueError("Unsupported verification_status")
    records = load_company_registry()
    query = q.casefold().strip() if q else None
    letter_filter = letter.casefold() if letter else None
    category_filter = category.casefold().strip() if category else None
    if category_filter == "business":
        category_filter = "enterprise"
    if category_filter and category_filter not in {"company", "enterprise", "corporate_group", "freelancer"}:
        raise ValueError("category must be one of: company, enterprise, corporate_group (legacy: business, freelancer)")
    filtered = []
    for record in records:
        name = str(record.get("name", "")).strip()
        searchable = " ".join([name] + [str(v) for v in record.get("aliases", [])] + [str(record.get("description", ""))]).casefold()
        if query and query not in searchable: continue
        if letter_filter and not name.casefold().startswith(letter_filter): continue
        if country and str(record.get("country_code", "")).casefold() != country.casefold(): continue
        if industry and industry.casefold() not in [str(v).casefold() for v in record.get("industries", [])]: continue
        if entity_type and str(record.get("entity_type", "")).casefold() != entity_type.casefold(): continue
        if verification_status and str(record.get("verification_status", "unverified")).casefold() != verification_status.casefold(): continue
        if category_filter and infer_record_type(record) != category_filter: continue
        filtered.append(record)
    filtered.sort(key=lambda x: (str(x.get("name", "")).casefold(), str(x.get("company_id", ""))))
    return {"total": len(filtered), "limit": limit, "offset": offset, "items": filtered[offset:offset + limit]}

def get_company(company_id: str) -> Optional[Dict[str, Any]]:
    return next((r for r in load_company_registry() if r.get("company_id") == company_id), None)

def get_company_alphabet() -> Dict[str, Any]:
    counts = {letter: 0 for letter in string.ascii_uppercase}
    for record in load_company_registry():
        first = str(record.get("name", "")).strip()[:1].upper()
        if first in counts: counts[first] += 1
    return {"total": sum(counts.values()), "letters": counts}

def load_country_sources() -> List[Dict[str, Any]]:
    source_path = PACKAGE_DIR / "data" / "country_sources.json"
    if not source_path.exists(): return []
    with source_path.open("r", encoding="utf-8") as f: payload = json.load(f)
    if not isinstance(payload, dict) or not isinstance(payload.get("sources"), list):
        raise ValueError("Country source registry must contain a sources list")
    seen = set()
    for i, source in enumerate(payload["sources"]):
        if not isinstance(source, dict): raise ValueError(f"Country source {i} must be an object")
        sid, code = str(source.get("source_id", "")).strip(), str(source.get("country_code", "")).strip()
        if not sid or not code: raise ValueError(f"Country source {i} requires source_id and country_code")
        if sid in seen: raise ValueError(f"Duplicate source_id: {sid}")
        seen.add(sid)
        if len(code) != 2 or not code.isalpha() or code != code.upper(): raise ValueError(f"Invalid ISO alpha-2 country_code for source {sid}")
        if not source.get("source_url"): raise ValueError(f"Country source {sid} requires source_url")
    return payload["sources"]

def list_country_sources(country_code: Optional[str] = None) -> Dict[str, Any]:
    sources = load_country_sources()
    if country_code: sources = [s for s in sources if s["country_code"] == country_code.upper()]
    sources.sort(key=lambda s: (s["country_name"].casefold(), s["name"].casefold()))
    countries = sorted({s["country_code"] for s in sources})
    return {"total": len(sources), "country_count": len(countries), "countries": countries, "items": sources, "registry_status": "source_directory_only"}

def get_country_source(source_id: str) -> Optional[Dict[str, Any]]:
    return next((s for s in load_country_sources() if s["source_id"] == source_id), None)

def get_api_status() -> Dict[str, Any]:
    records, sources = load_company_registry(), load_country_sources()
    count = len(records)
    return {
        "ecosystem": "GLOBAL COMPANY AND COMPANIES API",
        "status": "registry_empty" if count == 0 else "ready_with_records",
        "company_api": "ready" if count else "ready_empty_registry",
        "companies_api": "ready" if count else "ready_empty_registry",
        "registry_records": count,
        "source_count": len(sources),
        "source_countries": sorted({s["country_code"] for s in sources}),
        "registry_mode": "local_json_read_only",
        "source_mode": "official_source_directory_only",
        "note": "The registry is empty until sourced records are added. Country source entries are directory metadata, not live API connections. Verification requires traceable evidence."
    }
