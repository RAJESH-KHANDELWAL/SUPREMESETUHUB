"""Structural validation for authority directory entries; not legal verification."""
from urllib.parse import urlparse
from .categories import AUTHORITY_TYPES, AUTHORITY_RECORD_FIELDS

def validate_authority(record: dict) -> dict:
    missing = [key for key in AUTHORITY_RECORD_FIELDS if not record.get(key)]
    parsed = urlparse(record.get("official_website", ""))
    invalid_url = parsed.scheme != "https" or not parsed.netloc
    invalid_type = record.get("authority_type") not in AUTHORITY_TYPES
    return {"valid": not missing and not invalid_url and not invalid_type, "missing_fields": missing, "invalid_https_website": invalid_url, "invalid_authority_type": invalid_type, "legal_status_verified": False}
