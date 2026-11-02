"""Top-level Work & Careers API Ecosystem registry metadata."""
from .catalog import list_categories
from .professional_fields.catalog import list_professional_fields

def get_api_ecosystem() -> dict:
    categories, fields = list_categories(), list_professional_fields()
    return {"api_ecosystem_id": "WORK_CAREERS_EMPLOYMENT_API_ECOSYSTEM", "api_ecosystem_name": "Work & Careers Employment API Ecosystem", "taxonomy_status": "taxonomy_only", "coverage_scope": ["india", "global"], "employment_context_category_count": len(categories), "professional_field_count": len(fields), "professional_subcategory_count": sum(len(field.subcategories) for field in fields), "classification_axes": {"employment_context": "Employer sector, work arrangement, schedule, engagement type and career pathway.", "professional_occupation": "Professional field and occupation subcategory."}, "live_vacancies_verified": False, "employers_verified": False, "candidate_eligibility_verified": False}

def list_registry_categories() -> list[dict]:
    return [{"api_ecosystem_id": f"{item.id.upper()}_API_ECOSYSTEM", "category_id": item.id, "name": item.name, "category_type": item.category_type} for item in list_categories()]

def list_registry_professional_fields() -> list[dict]:
    return [{"api_ecosystem_id": f"{field.id.upper()}_PROFESSIONAL_FIELD_API_ECOSYSTEM", "field_id": field.id, "name": field.name, "subcategory_count": len(field.subcategories)} for field in list_professional_fields()]
