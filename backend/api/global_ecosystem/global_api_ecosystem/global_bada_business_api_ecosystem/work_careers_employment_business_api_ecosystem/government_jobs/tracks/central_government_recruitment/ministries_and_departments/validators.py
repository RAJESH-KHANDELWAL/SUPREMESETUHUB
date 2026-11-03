"""Structural checks for ministry/department records."""
from urllib.parse import urlparse
from .categories import DEPARTMENT_TYPES, EMPLOYMENT_DOMAINS

REQUIRED = ("id", "name", "department_type", "parent_ministry", "jurisdiction", "official_website", "recruiting_authority", "employment_domains")

def validate_department(record: dict) -> dict:
    missing = [key for key in REQUIRED if not record.get(key)]
    parsed = urlparse(record.get("official_website", ""))
    invalid_url = parsed.scheme != "https" or not parsed.netloc
    invalid_type = record.get("department_type") not in DEPARTMENT_TYPES
    invalid_domains = [value for value in record.get("employment_domains", []) if value not in EMPLOYMENT_DOMAINS]
    return {"valid": not missing and not invalid_url and not invalid_type and not invalid_domains, "missing_fields": missing, "invalid_https_website": invalid_url, "invalid_department_type": invalid_type, "invalid_employment_domains": invalid_domains, "recruitment_authority_verified": False}
