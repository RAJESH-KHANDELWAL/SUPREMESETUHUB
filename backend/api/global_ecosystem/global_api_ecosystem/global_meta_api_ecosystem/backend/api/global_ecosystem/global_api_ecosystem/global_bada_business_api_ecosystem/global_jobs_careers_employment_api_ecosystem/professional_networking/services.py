"""Service facade for one Jobs & Careers industry category."""
from .catalog import serialize_category
from .categories import CATEGORY_ID, get_category_definition, validate_category_definition


def get_category_resource() -> dict:
    return {"success": True, "category": serialize_category(), "taxonomy_status": "taxonomy_scaffold", "live_provider_data": False}


def list_subcategory_resources() -> list[dict]:
    item = get_category_definition()
    return [{"id": sid, "name": sid.replace("_", " ").title(), "category_id": CATEGORY_ID, "taxonomy_status": "taxonomy_scaffold"} for sid in item["subcategories"]]


def get_category_status() -> dict:
    integrity = validate_category_definition()
    return {"success": integrity["structurally_valid"], "category_id": CATEGORY_ID, "subcategory_count": integrity.get("subcategory_count", 0), "taxonomy_status": "taxonomy_scaffold", "live_provider_data": False, **integrity}
