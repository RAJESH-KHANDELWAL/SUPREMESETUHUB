"""Read-only taxonomy services for real estate facilities."""
from .categories import FIELD_ID, FIELD_NAME, FIELD_DESCRIPTION, SUBCATEGORY_DEFINITIONS

def list_subcategories() -> list[dict]:
    return [dict(item) for item in SUBCATEGORY_DEFINITIONS]

def get_subcategory(subcategory_id: str) -> dict | None:
    return next((dict(item) for item in SUBCATEGORY_DEFINITIONS if item["id"] == subcategory_id), None)

def search_subcategories(query: str) -> list[dict]:
    needle = query.strip().casefold()
    if not needle:
        return []
    return [dict(item) for item in SUBCATEGORY_DEFINITIONS if any(needle in str(item[key]).casefold() for key in ("id", "name", "description"))]
