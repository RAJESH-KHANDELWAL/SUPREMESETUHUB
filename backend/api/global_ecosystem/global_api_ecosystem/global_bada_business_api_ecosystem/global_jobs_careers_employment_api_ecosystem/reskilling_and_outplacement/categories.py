"""Independent API package for one Jobs, Careers & Employment industry category."""
from importlib import import_module

CATEGORY_ID = __package__.rsplit(".", 1)[-1]
DOMAIN_PACKAGE = __package__.rsplit(".", 1)[0]


def get_category_definition() -> dict:
    """Resolve this category from the domain's canonical catalogue."""
    catalog = import_module(f"{DOMAIN_PACKAGE}.catalog")
    item = catalog.get_category(CATEGORY_ID)
    if item is None:
        raise LookupError(f"Unknown Jobs & Careers category: {CATEGORY_ID}")
    return item


def validate_category_definition() -> dict:
    try:
        item = get_category_definition()
    except LookupError as exc:
        return {"category_id": CATEGORY_ID, "structurally_valid": False, "errors": [str(exc)]}
    subcategories = item.get("subcategories", [])
    errors = []
    if not item.get("name"):
        errors.append("Category name is required.")
    if not subcategories:
        errors.append("At least one canonical subcategory is required.")
    if len(subcategories) != len(set(subcategories)):
        errors.append("Duplicate subcategory IDs found.")
    return {
        "category_id": CATEGORY_ID,
        "subcategory_count": len(subcategories),
        "structurally_valid": not errors,
        "errors": errors,
        "taxonomy_status": "taxonomy_scaffold",
    }
