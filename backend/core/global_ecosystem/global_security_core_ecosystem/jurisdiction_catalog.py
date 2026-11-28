"""Jurisdiction profile catalog; profile registration is not legal compliance."""
from __future__ import annotations
from copy import deepcopy
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_PROFILES = (
    ("IN", "India", "jurisdictions/india/jurisdiction_manifest.json"),
    ("GLOBAL", "Cross-border and international reference", "jurisdictions/global/jurisdiction_manifest.json"),
)

def _load_profiles():
    result = []
    for jurisdiction_id, name, relative_path in _PROFILES:
        path = (_ROOT / relative_path).resolve()
        if _ROOT not in path.parents or not path.is_file():
            raise ValueError(f"JURISDICTION_PROFILE_MISSING: {jurisdiction_id}")
        profile = json.loads(path.read_text(encoding="utf-8"))
        if profile.get("jurisdiction_id") != jurisdiction_id:
            raise ValueError(f"JURISDICTION_PROFILE_ID_MISMATCH: {jurisdiction_id}")
        if profile.get("status") != "PROFILE_METADATA_ONLY":
            raise ValueError(f"JURISDICTION_PROFILE_STATUS_INVALID: {jurisdiction_id}")
        result.append({"jurisdiction_id": jurisdiction_id, "name": name, "manifest_path": relative_path, "status": profile["status"], "legal_review_required": True})
    return tuple(result)

JURISDICTIONS = _load_profiles()

def get_jurisdictions():
    return deepcopy(list(JURISDICTIONS))

def get_jurisdiction(jurisdiction_id: str):
    needle = jurisdiction_id.strip().upper()
    for item in JURISDICTIONS:
        if item["jurisdiction_id"] == needle:
            return deepcopy(item)
    return None

def jurisdiction_summary():
    return {"jurisdiction_profile_count": len(JURISDICTIONS), "legal_compliance_verified": False}
