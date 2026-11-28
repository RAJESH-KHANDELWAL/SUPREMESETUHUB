"""Domain services for Office and Remote Hybrid Roles."""
from .categories import CATEGORY_ID, JOB_FAMILY_ID, JOB_FAMILY_NAME, REQUIRED_DOMAIN_FIELDS, ROLE_EXAMPLES
from .validators import validate_domain_details, validate_source_provenance

def get_job_family() -> dict:
    return {"category_id": CATEGORY_ID, "job_family_id": JOB_FAMILY_ID, "name": JOB_FAMILY_NAME, "role_examples": list(ROLE_EXAMPLES), "required_domain_fields": list(REQUIRED_DOMAIN_FIELDS), "taxonomy_status": "taxonomy_only"}

def validate_job_work_record(payload: dict) -> dict:
    errors = validate_domain_details(payload.get("domain_details", {}))
    errors.extend(validate_source_provenance(payload.get("source_url"), payload.get("last_verified_at")))
    return {"valid": not errors, "errors": errors}
