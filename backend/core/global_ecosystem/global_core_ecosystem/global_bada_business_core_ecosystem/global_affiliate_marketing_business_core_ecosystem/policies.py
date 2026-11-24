"""Business rules for affiliate disclosures and program activation."""
from __future__ import annotations

from urllib.parse import urlparse

SUPPORTED_COMMISSION_TYPES = frozenset({"PERCENTAGE", "FIXED", "UNSPECIFIED"})
SUPPORTED_PROGRAM_STATUSES = frozenset({
    "PENDING_VERIFICATION", "ACTIVE", "PAUSED", "ARCHIVED",
})
SUPPORTED_VERIFICATION_STATUSES = frozenset({
    "UNVERIFIED", "PENDING", "VERIFIED", "REJECTED",
})
SUPPORTED_EVENT_TYPES = frozenset({"CLICK", "LEAD", "CONVERSION"})


def validate_http_url(value: str, field_name: str = "URL") -> str:
    """Accept only absolute HTTP(S) URLs; reject javascript:, file:, and blanks."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name}_REQUIRED")
    parsed = urlparse(value.strip())
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"{field_name}_MUST_BE_HTTP_OR_HTTPS")
    return value.strip()


def validate_affiliate_disclosure(value: str) -> str:
    """Require a visible, plain-language statement that compensation may occur.

    This is a minimum product guardrail, not a legal-compliance certification.
    """
    if not isinstance(value, str) or len(value.strip()) < 15:
        raise ValueError("AFFILIATE_DISCLOSURE_REQUIRED")
    text = value.strip().lower()
    disclosure_terms = ("affiliate", "commission", "paid", "earn", "compensation")
    if not any(term in text for term in disclosure_terms):
        raise ValueError("AFFILIATE_DISCLOSURE_MUST_EXPLAIN_POTENTIAL_COMPENSATION")
    return value.strip()


def validate_program_activation(
    program_status: str,
    verification_status: str,
    terms_url: str | None,
) -> None:
    """Do not mark an affiliate program active until its terms are verified."""
    if program_status == "ACTIVE":
        if verification_status != "VERIFIED":
            raise ValueError("AFFILIATE_PROGRAM_MUST_BE_VERIFIED_BEFORE_ACTIVATION")
        validate_http_url(terms_url or "", "TERMS_URL")


__all__ = [
    "SUPPORTED_COMMISSION_TYPES", "SUPPORTED_PROGRAM_STATUSES",
    "SUPPORTED_VERIFICATION_STATUSES", "SUPPORTED_EVENT_TYPES",
    "validate_http_url", "validate_affiliate_disclosure",
    "validate_program_activation",
]
