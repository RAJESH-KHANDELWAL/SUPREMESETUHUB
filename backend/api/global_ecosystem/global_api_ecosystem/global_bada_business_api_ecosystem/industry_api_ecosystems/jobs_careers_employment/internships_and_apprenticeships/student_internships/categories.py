"""Canonical binding for one subcategory; parent domain catalogue is source of truth."""
from importlib import import_module

SUBCATEGORY_ID = __package__.rsplit(".", 1)[-1]
CATEGORY_PACKAGE = __package__.rsplit(".", 1)[0]
CATEGORY_ID = CATEGORY_PACKAGE.rsplit(".", 1)[-1]
DOMAIN_PACKAGE = CATEGORY_PACKAGE.rsplit(".", 1)[0]


def get_subcategory_definition() -> dict:
    catalog = import_module(f"{DOMAIN_PACKAGE}.catalog")
    category = catalog.get_category(CATEGORY_ID)
    if category is None:
        raise LookupError(f"Unknown parent Jobs & Careers category: {CATEGORY_ID}")
    if SUBCATEGORY_ID not in category.get("subcategories", []):
        raise LookupError(f"Subcategory '{SUBCATEGORY_ID}' is not registered under '{CATEGORY_ID}'.")
    return {"id": SUBCATEGORY_ID, "name": SUBCATEGORY_ID.replace("_", " ").title(), "category_id": CATEGORY_ID, "taxonomy_status": "taxonomy_scaffold"}


def validate_subcategory_definition() -> dict:
    try:
        item = get_subcategory_definition()
    except LookupError as exc:
        return {"category_id": CATEGORY_ID, "subcategory_id": SUBCATEGORY_ID, "structurally_valid": False, "errors": [str(exc)], "taxonomy_status": "taxonomy_scaffold"}
    return {"category_id": CATEGORY_ID, "subcategory_id": SUBCATEGORY_ID, "structurally_valid": bool(item["name"]), "errors": [], "taxonomy_status": "taxonomy_scaffold"}
