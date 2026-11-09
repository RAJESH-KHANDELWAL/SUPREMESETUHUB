"""Compatibility exports for the canonical Government, Public Services & Social Impact catalog."""
from ..government_public_services_social_impact.catalog import (
    CATEGORIES,
    LEGACY_CATEGORY_CROSSWALK,
    list_categories,
    get_category,
)

def search_categories(query: str, include_restricted: bool = False):
    term = query.strip().casefold()
    return [
        item for item in list_categories()
        if term and (term in item["id"].casefold()
                     or term in item["name"].casefold()
                     or any(term in sub.replace("_", " ").casefold()
                            for sub in item["subcategories"]))
    ]

def get_catalogue_metadata():
    return {
        "domain_id": "government_public_services_social_impact",
        "domain_name": "Government, Public Services & Social Impact API Ecosystem",
        "category_count": len(CATEGORIES),
        "adult_restricted": False,
        "default_discovery_enabled": True,
        "catalogue_status": "taxonomy_only",
        "compatibility_facade": True,
    }
