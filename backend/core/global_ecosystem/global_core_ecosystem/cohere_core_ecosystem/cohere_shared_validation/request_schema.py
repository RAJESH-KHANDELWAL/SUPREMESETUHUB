"""Dependency-free provider request shape validation."""
from __future__ import annotations

from collections.abc import Mapping


def validate_payload(payload, required=()):
    if not isinstance(payload, Mapping):
        return False, ("payload must be a mapping",)
    missing = tuple(key for key in required if key not in payload)
    return not missing, tuple(f"missing required field: {key}" for key in missing)


def require_non_empty_string(value, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")
    return value


def require_string_sequence(value, field: str) -> tuple[str, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, (list, tuple)):
        raise ValueError(f"{field} must be a list or tuple of strings")
    if not value or any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValueError(f"{field} must contain non-empty strings")
    return tuple(value)
