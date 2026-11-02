"""Work, Jobs & Careers domain package; taxonomy only, not verified live listings."""
from .categories import (
    ADULT_RESTRICTED,
    CATEGORY_DEFINITIONS,
    DEFAULT_DISCOVERY_ENABLED,
    DOMAIN_ID,
    DOMAIN_NAME,
    SUBCATEGORY_IDS,
)

def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and display labels for registry compatibility."""
    return [
        {"id": item["id"], "name": item["name"], "domain_id": DOMAIN_ID}
        for item in CATEGORY_DEFINITIONS
    ]

__all__ = [
    "DOMAIN_ID", "DOMAIN_NAME", "ADULT_RESTRICTED",
    "DEFAULT_DISCOVERY_ENABLED", "SUBCATEGORY_IDS",
    "CATEGORY_DEFINITIONS", "list_subcategories",
]
