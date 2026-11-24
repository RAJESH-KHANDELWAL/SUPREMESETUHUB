"""Validation rules for Returnship Placements records."""
from .categories import REQUIRED_DOMAIN_FIELDS

def validate_domain_details(details: dict[str, str]) -> list[str]:
    return [f"Missing required domain field: {field}" for field in REQUIRED_DOMAIN_FIELDS if field not in details or not str(details[field]).strip()]

def validate_source_provenance(source_url: str | None, last_verified_at: str | None) -> list[str]:
    errors = []
    if source_url and not source_url.startswith(("https://", "http://")):
        errors.append("source_url must be an HTTP(S) URL")
    if source_url and not last_verified_at:
        errors.append("last_verified_at is required when source_url is supplied")
    return errors
