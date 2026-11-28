"""Work, Jobs & Careers API Ecosystem domain package."""
from .categories import (
    ADULT_RESTRICTED,
    CATEGORY_DEFINITIONS,
    CATEGORY_IDS,
    DEFAULT_DISCOVERY_ENABLED,
    DOMAIN_ID,
    DOMAIN_NAME,
    SUBCATEGORY_IDS,  # compatibility alias for the shared legacy domain registry
)

def list_categories() -> list[dict[str, str]]:
    """Return stable category API Ecosystem IDs and display labels."""
    return [
        {"id": item["id"], "name": item["name"], "domain_id": DOMAIN_ID}
        for item in CATEGORY_DEFINITIONS
    ]

__all__ = [
    "DOMAIN_ID", "DOMAIN_NAME", "ADULT_RESTRICTED",
    "DEFAULT_DISCOVERY_ENABLED", "CATEGORY_IDS", "CATEGORY_DEFINITIONS",
    "list_categories", "SUBCATEGORY_IDS",
]
