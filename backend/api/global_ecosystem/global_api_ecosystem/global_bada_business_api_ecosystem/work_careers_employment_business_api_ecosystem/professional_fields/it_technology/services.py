"""Read-only taxonomy operations for IT & Digital Technology."""
from .categories import FIELD_ID, SUBCATEGORY_DEFINITIONS

def list_subcategories() -> list[dict]:
    return [dict(item) for item in SUBCATEGORY_DEFINITIONS]

def get_subcategory(subcategory_id: str) -> dict | None:
    return next((dict(item) for item in SUBCATEGORY_DEFINITIONS if item["id"] == subcategory_id), None)
