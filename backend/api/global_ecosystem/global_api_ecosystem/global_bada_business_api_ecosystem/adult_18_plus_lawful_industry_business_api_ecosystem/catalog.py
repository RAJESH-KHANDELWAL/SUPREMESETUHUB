"""Structured category catalogue for adult_18_plus_lawful_industry."""
from . import DOMAIN_ID, DOMAIN_NAME, ADULT_RESTRICTED, SUBCATEGORY_IDS
from .models import CategoryRecord
CATEGORIES = tuple(CategoryRecord(value, value.replace("_", " ").title(), DOMAIN_ID, ADULT_RESTRICTED) for value in SUBCATEGORY_IDS)
def list_categories(include_restricted: bool = False):
    if ADULT_RESTRICTED and not include_restricted:
        return []
    return list(CATEGORIES)
def get_category(category_id: str, include_restricted: bool = False):
    if ADULT_RESTRICTED and not include_restricted:
        return None
    return next((item for item in CATEGORIES if item.id == category_id), None)
def search_categories(query: str, include_restricted: bool = False):
    term = query.strip().casefold()
    if ADULT_RESTRICTED and not include_restricted:
        return []
    return [item for item in CATEGORIES if term and (term in item.id.casefold() or term in item.name.casefold())]
def get_catalogue_metadata():
    return {"domain_id": DOMAIN_ID, "domain_name": DOMAIN_NAME, "category_count": len(CATEGORIES), "adult_restricted": ADULT_RESTRICTED, "default_discovery_enabled": not ADULT_RESTRICTED, "catalogue_status": "taxonomy_only"}
