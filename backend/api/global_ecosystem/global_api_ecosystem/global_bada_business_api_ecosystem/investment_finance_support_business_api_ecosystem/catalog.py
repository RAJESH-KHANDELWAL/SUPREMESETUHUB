"""Compatibility catalogue backed by the canonical finance ecosystem."""
from ..global_finance_banking_insurance_api_ecosystem.catalog import (
    list_categories as _list_categories, get_category as _get_category,
    LEGACY_CATEGORY_CROSSWALK,
)
from . import DOMAIN_ID, DOMAIN_NAME, ADULT_RESTRICTED, SUBCATEGORY_IDS

def list_categories(include_restricted: bool = False):
    return _list_categories()

def get_category(category_id: str, include_restricted: bool = False):
    canonical_id = LEGACY_CATEGORY_CROSSWALK.get(category_id, category_id)
    return _get_category(canonical_id)

def search_categories(query: str, include_restricted: bool = False):
    term = query.strip().casefold()
    return [item for item in _list_categories() if term in item["id"].casefold() or term in item["name"].casefold() or any(term in sub.replace("_", " ").casefold() for sub in item["subcategories"])]

def get_catalogue_metadata():
    return {"domain_id": DOMAIN_ID, "domain_name": DOMAIN_NAME, "category_count": len(_list_categories()), "adult_restricted": False, "default_discovery_enabled": True, "catalogue_status": "taxonomy_only", "canonical_domain_id": "finance_banking_insurance"}
