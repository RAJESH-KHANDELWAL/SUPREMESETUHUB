"""Structured subcategory catalogue for students_education_skills."""
from . import DOMAIN_ID, DOMAIN_NAME, ADULT_RESTRICTED, SUBCATEGORY_IDS
from .models import CategoryRecord

CATEGORIES = tuple(CategoryRecord(
    id=value,
    name=value.replace("_", " ").title(),
    domain_id=DOMAIN_ID,
    adult_restricted=ADULT_RESTRICTED,
) for value in SUBCATEGORY_IDS)

def list_categories():
    return [record for record in CATEGORIES]

def get_category(category_id: str):
    return next((record for record in CATEGORIES if record.id == category_id), None)

def search_categories(query: str):
    needle = query.strip().casefold()
    if not needle:
        return []
    return [record for record in CATEGORIES if needle in record.id.casefold() or needle in record.name.casefold()]

def get_catalogue_metadata():
    return {"domain_id": DOMAIN_ID, "domain_name": DOMAIN_NAME, "category_count": len(CATEGORIES), "adult_restricted": ADULT_RESTRICTED, "catalogue_status": "taxonomy_only"}
