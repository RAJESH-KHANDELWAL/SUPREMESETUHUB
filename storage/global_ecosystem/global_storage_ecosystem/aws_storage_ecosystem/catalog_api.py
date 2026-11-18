"""Read-only catalog helpers for AWS storage category metadata."""
from .ecosystem_taxonomy import load_taxonomy

def list_categories() -> list[dict]:
    return list(load_taxonomy().get("categories", []))

def get_category(category_id: str) -> dict | None:
    key = category_id.strip().upper()
    return next((item for item in list_categories() if item["category"] == key), None)
