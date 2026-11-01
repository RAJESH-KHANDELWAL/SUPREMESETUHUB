"""Read-only platform taxonomy and source-aware profile directory."""
import json
from pathlib import Path
from typing import Any, Optional
from .catalog import PLATFORM_DOMAINS, PLATFORM_TYPES, OWNERSHIP_TYPES, BUSINESS_MODELS, VERIFICATION_STATES
PACKAGE_DIR = Path(__file__).resolve().parent
REGISTRY_PATH = PACKAGE_DIR / "data" / "platform_registry.json"

def load_platform_registry() -> list[dict[str, Any]]:
    """Load canonical platform profiles; a missing registry is an empty directory."""
    if not REGISTRY_PATH.exists(): return []
    with REGISTRY_PATH.open("r", encoding="utf-8") as stream: payload = json.load(stream)
    if not isinstance(payload, dict) or not isinstance(payload.get("records", []), list): raise ValueError("Platform registry must contain a records list")
    records = payload.get("records", []); seen = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict): raise ValueError(f"Platform record {index} must be an object")
        pid, name = str(record.get("platform_id", "")).strip(), str(record.get("name", "")).strip()
        if not pid or not name: raise ValueError(f"Platform record {index} requires platform_id and name")
        if pid in seen: raise ValueError(f"Duplicate platform_id: {pid}")
        seen.add(pid); status = record.get("verification_status", "unverified")
        if status not in VERIFICATION_STATES: raise ValueError(f"Unsupported verification status for {pid}")
        if status in {"source_checked", "identity_verified", "operator_verified"} and not record.get("source_urls"): raise ValueError(f"Verified platform {pid} requires source_urls")
        if record.get("adult_only") and int(record.get("minimum_age", 0)) < 18: raise ValueError(f"Adult platform {pid} must require age 18 or above")
    return records

def get_ecosystem_status() -> dict[str, Any]:
    records = load_platform_registry()
    return {"ecosystem":"GLOBAL PLATFORMS API ECOSYSTEM","status":"ready_with_records" if records else "registry_empty","profile_count":len(records),"domain_count":len(PLATFORM_DOMAINS),"platform_type_count":len(PLATFORM_TYPES),"registry_mode":"local_json_read_only","taxonomy_mode":"curated_metadata","live_external_connections":False,"note":"Taxonomy availability does not imply live integrations or complete global coverage."}

def list_domains(include_adult: bool = False) -> list[dict[str, Any]]:
    return [d for d in PLATFORM_DOMAINS if include_adult or not d.get("adult_only", False)]

def get_domain(domain_id: str) -> Optional[dict[str, Any]]:
    return next((d for d in PLATFORM_DOMAINS if d["domain_id"] == domain_id), None)

def search_platforms(q: Optional[str] = None, domain: Optional[str] = None, country: Optional[str] = None, platform_type: Optional[str] = None, verification_status: Optional[str] = None, include_adult: bool = False, limit: int = 50, offset: int = 0) -> dict[str, Any]:
    if limit < 1 or limit > 200 or offset < 0: raise ValueError("limit must be 1..200 and offset non-negative")
    query = q.casefold().strip() if q else None; results = []
    for record in load_platform_registry():
        if record.get("adult_only") and not include_adult: continue
        searchable = " ".join([str(record.get("name","")), str(record.get("description","")), *[str(x) for x in record.get("aliases",[])]]).casefold()
        if query and query not in searchable: continue
        if domain and str(record.get("domain_id","")).casefold() != domain.casefold(): continue
        if country and country.upper() not in [str(x).upper() for x in record.get("country_codes",[])]: continue
        if platform_type and str(record.get("platform_type","")).casefold() != platform_type.casefold(): continue
        if verification_status and str(record.get("verification_status","unverified")).casefold() != verification_status.casefold(): continue
        results.append(record)
    results.sort(key=lambda x:(str(x.get("name","")).casefold(),str(x.get("platform_id",""))))
    return {"total":len(results),"limit":limit,"offset":offset,"include_adult":include_adult,"items":results[offset:offset+limit]}

def get_platform(platform_id: str, include_adult: bool = False) -> Optional[dict[str, Any]]:
    record = next((r for r in load_platform_registry() if r["platform_id"] == platform_id), None)
    return None if record and record.get("adult_only") and not include_adult else record
