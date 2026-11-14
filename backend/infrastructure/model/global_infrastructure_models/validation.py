"""Validation helpers for normalized infrastructure resource records."""
from __future__ import annotations
from collections.abc import Mapping
REQUIRED_RESOURCE_FIELDS = ("resource_id", "resource_type", "category")
def validate_resource_record(record: Mapping) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_RESOURCE_FIELDS:
        value = record.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field} must be a non-empty string")
    metadata = record.get("metadata", {})
    if metadata is not None and not isinstance(metadata, Mapping):
        errors.append("metadata must be a mapping when provided")
    return errors
