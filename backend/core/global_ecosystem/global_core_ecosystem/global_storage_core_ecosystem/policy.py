"""CORE metadata policy for storage provider discovery."""
from __future__ import annotations

from typing import Any

SENSITIVE_KEY_FRAGMENTS = ("secret", "password", "token", "credential", "private_key", "access_key")
ALLOWED_READINESS = {
    "CORE_CATALOG_ONLY", "CORE_METADATA_AVAILABLE", "READY_FOR_CONFIGURATION",
    "READY", "DISABLED", "ERROR",
}


def redact_metadata(value: Any) -> Any:
    """Recursively redact secret-like keys from metadata before returning it."""
    if isinstance(value, dict):
        clean = {}
        for key, item in value.items():
            key_text = str(key).lower()
            if any(fragment in key_text for fragment in SENSITIVE_KEY_FRAGMENTS):
                clean[str(key)] = "[REDACTED]"
            else:
                clean[str(key)] = redact_metadata(item)
        return clean
    if isinstance(value, list):
        return [redact_metadata(item) for item in value]
    if isinstance(value, tuple):
        return [redact_metadata(item) for item in value]
    return value


def validate_provider_metadata(payload: dict[str, Any]) -> None:
    if not isinstance(payload, dict):
        raise TypeError("PROVIDER_METADATA_MUST_BE_OBJECT")
    readiness = payload.get("readiness", "CORE_CATALOG_ONLY")
    if readiness not in ALLOWED_READINESS:
        raise ValueError("INVALID_PROVIDER_READINESS")
    if payload.get("api_available") is True and payload.get("connection_verified") is not True:
        raise ValueError("UNVERIFIED_PROVIDER_CANNOT_BE_MARKED_AVAILABLE")
    if any(fragment in str(key).lower() for key in payload
           for fragment in ("secret_value", "password_value", "private_key_value")):
        raise ValueError("RAW_SECRET_MATERIAL_FORBIDDEN_IN_CORE_METADATA")


__all__ = ["redact_metadata", "validate_provider_metadata", "ALLOWED_READINESS"]
