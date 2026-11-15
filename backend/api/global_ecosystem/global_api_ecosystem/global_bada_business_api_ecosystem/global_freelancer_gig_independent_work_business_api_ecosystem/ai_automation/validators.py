"""Integrity checks for the ai_automation work-type catalogue."""
from .work_types import WORK_TYPES

def validate_work_types():
    ids = [item.get("id", "") for item in WORK_TYPES]
    names = [item.get("name", "").strip() for item in WORK_TYPES]
    duplicate_ids = sorted({value for value in ids if ids.count(value) > 1})
    invalid = [item.get("id", "") for item in WORK_TYPES if not item.get("id") or not item.get("name", "").strip() or not item.get("description", "").strip()]
    return {"specialization_id": "ai_automation", "work_type_count": len(WORK_TYPES), "duplicate_ids": duplicate_ids, "invalid_records": invalid, "structurally_valid": bool(WORK_TYPES) and not duplicate_ids and not invalid and len(names) == len(set(names))}
