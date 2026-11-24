"""Independent Professional Field API Ecosystem contract for real_estate_facilities."""
from .categories import FIELD_ID, FIELD_NAME, FIELD_DESCRIPTION, SUBCATEGORY_DEFINITIONS

def get_api_ecosystem() -> dict:
    return {"api_ecosystem_id": f"{FIELD_ID.upper()}_PROFESSIONAL_FIELD_API_ECOSYSTEM", "api_ecosystem_name": f"{FIELD_NAME} API Ecosystem", "parent_api_ecosystem_id": "PROFESSIONAL_FIELDS_API_ECOSYSTEM", "parent_domain_api_ecosystem_id": "WORK_CAREERS_EMPLOYMENT_API_ECOSYSTEM", "field_id": FIELD_ID, "field_name": FIELD_NAME, "description": FIELD_DESCRIPTION, "taxonomy_status": "taxonomy_only", "subcategory_count": len(SUBCATEGORY_DEFINITIONS), "capabilities": ["status", "occupation_list", "occupation_detail", "occupation_search", "integrity"], "vacancies_verified": False, "employers_verified": False, "credentials_verified": False}

def list_subcategory_api_ecosystems() -> list[dict]:
    return [{"api_ecosystem_id": f"{FIELD_ID.upper()}_{item['id'].upper()}_PROFESSIONAL_SUBCATEGORY_API_ECOSYSTEM", "api_ecosystem_name": f"{item['name']} API Ecosystem", "parent_api_ecosystem_id": f"{FIELD_ID.upper()}_PROFESSIONAL_FIELD_API_ECOSYSTEM", "field_id": FIELD_ID, "subcategory_id": item["id"], "name": item["name"], "description": item["description"], "taxonomy_status": "taxonomy_only"} for item in SUBCATEGORY_DEFINITIONS]
