"""Service layer for professional-field taxonomy."""
from dataclasses import asdict
from .catalog import list_professional_fields, get_professional_field, list_professional_subcategories, get_professional_subcategory, validate_professional_fields

def search_professional_fields(query: str) -> list[dict]:
    needle = query.strip().casefold()
    if not needle:
        return []
    results = []
    for field in list_professional_fields():
        matches = [asdict(sub) for sub in field.subcategories if needle in sub.id.casefold() or needle in sub.name.casefold() or needle in sub.description.casefold()]
        if needle in field.id.casefold() or needle in field.name.casefold() or needle in field.description.casefold() or matches:
            results.append({"field": {"id": field.id, "name": field.name, "description": field.description}, "matching_subcategories": matches})
    return results

def get_professional_fields_status() -> dict:
    return {"success": True, **validate_professional_fields(), "live_vacancies_verified": False, "professional_credentials_verified": False}
