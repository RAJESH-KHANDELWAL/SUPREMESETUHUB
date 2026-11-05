"""API ecosystem descriptor for Technical Architecture Roles."""
from .services import get_job_family
from .validators import validate_domain_details

def get_api_ecosystem() -> dict:
    family = get_job_family()
    return {"api_ecosystem_id": f"{family['category_id'].upper()}_{family['job_family_id'].upper()}_API", "api_ecosystem_name": f"{family['name']} API", "parent_category_id": family["category_id"], "job_family": family, "integrity": {"required_domain_fields": family["required_domain_fields"], "validator_available": callable(validate_domain_details)}, "taxonomy_status": "taxonomy_only", "live_vacancies_verified": False}
