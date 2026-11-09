"""Service facade for one independently addressable industry subcategory."""
from .catalog import serialize_subcategory
from .categories import CATEGORY_ID, SUBCATEGORY_ID, validate_subcategory_definition


def get_subcategory_resource() -> dict:
    return {"success": True, "subcategory": serialize_subcategory(), "taxonomy_status": "taxonomy_scaffold", "live_provider_data": False}


def get_subcategory_status() -> dict:
    integrity = validate_subcategory_definition()
    return {"success": integrity["structurally_valid"], "category_id": CATEGORY_ID, "subcategory_id": SUBCATEGORY_ID, "taxonomy_status": "taxonomy_scaffold", "live_provider_data": False, **integrity}
