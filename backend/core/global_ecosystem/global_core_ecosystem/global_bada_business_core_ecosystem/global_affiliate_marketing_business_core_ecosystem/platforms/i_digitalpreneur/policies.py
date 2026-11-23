"""iDigitalPreneur-specific identity and program-boundary policies."""
from __future__ import annotations

from typing import Any

from ..policies import (
    validate_affiliate_disclosure,
    validate_http_url,
    validate_program_activation,
)

PLATFORM_ID = "I-DIGITALPRENEUR"

def validate_platform_id(platform_id: str) -> str:
    if not isinstance(platform_id, str) or platform_id.strip().upper() != PLATFORM_ID:
        raise ValueError("IDIGITALPRENEUR_PLATFORM_ID_MISMATCH")
    return PLATFORM_ID

def validate_platform_program(
    *,
    platform_id: str,
    program_status: str,
    verification_status: str,
    terms_url: str | None,
) -> dict[str, Any]:
    """Apply shared program invariants while keeping platform identity fixed."""
    validate_platform_id(platform_id)
    validate_program_activation(program_status, verification_status, terms_url)
    normalized_url = validate_http_url(terms_url, "TERMS_URL") if terms_url else None
    return {
        "platform_id": PLATFORM_ID,
        "program_status": program_status.strip().upper(),
        "verification_status": verification_status.strip().upper(),
        "terms_url": normalized_url,
    }

__all__ = [
    "PLATFORM_ID", "validate_platform_id", "validate_platform_program",
    "validate_affiliate_disclosure", "validate_http_url",
]
