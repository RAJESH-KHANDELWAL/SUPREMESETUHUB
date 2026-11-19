"""Validation and governance rules for culture-service-work-business records."""
from __future__ import annotations
from typing import Any
from .catalog import get_capability

ALLOWED_STATUSES = {"DRAFT", "SUBMITTED", "REVIEWED", "APPROVED", "REJECTED", "ARCHIVED"}

def validate_record(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in ("record_id", "capability_id", "title", "description", "record_type"):
        if not str(record.get(field, "")).strip():
            errors.append(f"{field.upper()}_REQUIRED")
    capability = get_capability(str(record.get("capability_id", "")))
    if record.get("capability_id") and capability is None:
        errors.append("UNKNOWN_CULTURAL_CAPABILITY")
    status = str(record.get("status", "DRAFT")).upper()
    if status not in ALLOWED_STATUSES:
        errors.append("INVALID_RECORD_STATUS")
    if record.get("source_url") and not str(record["source_url"]).startswith(("https://", "http://")):
        errors.append("SOURCE_URL_MUST_BE_HTTP_OR_HTTPS")
    return errors

def publication_allowed(record: dict[str, Any]) -> bool:
    return not validate_record(record) and str(record.get("status", "DRAFT")).upper() == "APPROVED"
