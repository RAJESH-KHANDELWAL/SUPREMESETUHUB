"""Read-only taxonomy services for Education & Training."""
from .categories import SUBCATEGORY_DEFINITIONS
def list_subcategories() -> list[dict]:
    return [dict(item) for item in SUBCATEGORY_DEFINITIONS]
def get_subcategory(subcategory_id: str) -> dict | None:
    return next((dict(item) for item in SUBCATEGORY_DEFINITIONS if item["id"] == subcategory_id), None)
