"""Structural checks for Government Jobs notice provenance.

These checks validate required fields and HTTPS URL shape only. They do not authenticate
a website, confirm an open vacancy, interpret recruitment law, or determine eligibility.
"""
from urllib.parse import urlparse

REQUIRED_NOTICE_FIELDS = (
    "notice_id", "title", "issuing_authority", "jurisdiction",
    "official_notice_url", "notice_or_advertisement_id",
    "publication_date", "last_verified_at", "verification_status",
)
ALLOWED_VERIFICATION_STATUSES = {
    "unverified", "source_checked", "authority_confirmed", "expired", "withdrawn",
}

def validate_notice_record(record: dict) -> dict:
    missing = [
        field for field in REQUIRED_NOTICE_FIELDS
        if not isinstance(record.get(field), str) or not record[field].strip()
    ]
    url = record.get("official_notice_url", "")
    parsed = urlparse(url) if isinstance(url, str) else None
    invalid_url = not parsed or parsed.scheme != "https" or not parsed.netloc
    invalid_status = record.get("verification_status") not in ALLOWED_VERIFICATION_STATUSES
    return {
        "valid": not missing and not invalid_url and not invalid_status,
        "missing_fields": missing,
        "official_notice_url_must_be_https": invalid_url,
        "invalid_verification_status": invalid_status,
        "authenticity_verified": False,
        "legal_eligibility_verified": False,
    }
