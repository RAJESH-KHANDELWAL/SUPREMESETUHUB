"""Structured category catalogue for home_homemaker_care_economy."""
from . import DOMAIN_ID, DOMAIN_NAME, ADULT_RESTRICTED, SUBCATEGORY_IDS
from .models import CategoryRecord
CATEGORIES = tuple(CategoryRecord(value, value.replace("_", " ").title(), DOMAIN_ID, ADULT_RESTRICTED) for value in SUBCATEGORY_IDS)
def list_categories():
    return list(CATEGORIES)
def get_category(category_id: str):
    return next((item for item in CATEGORIES if item.id == category_id), None)
def search_categories(query: str):
    term = query.strip().casefold()
    return [item for item in CATEGORIES if term and (term in item.id.casefold() or term in item.name.casefold())]
def get_catalogue_metadata():
    return {"domain_id": DOMAIN_ID, "domain_name": DOMAIN_NAME, "category_count": len(CATEGORIES), "adult_restricted": ADULT_RESTRICTED, "catalogue_status": "taxonomy_only"}
