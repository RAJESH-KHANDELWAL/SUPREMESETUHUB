"""Structural validation for manufacturing_operations taxonomy definitions."""
from .categories import FIELD_ID, FIELD_NAME, FIELD_DESCRIPTION, SUBCATEGORY_DEFINITIONS

def validate_field_taxonomy() -> dict:
    ids = [item.get("id", "") for item in SUBCATEGORY_DEFINITIONS]
    duplicates = sorted({value for value in ids if ids.count(value) > 1})
    invalid = [item.get("id", "<missing>") for item in SUBCATEGORY_DEFINITIONS if not item.get("id") or not item.get("name") or not item.get("description")]
    return {
        "field_id": FIELD_ID,
        "field_name": FIELD_NAME,
        "subcategory_count": len(SUBCATEGORY_DEFINITIONS),
        "duplicate_subcategory_ids": duplicates,
        "invalid_subcategories": invalid,
        "structurally_valid": bool(FIELD_ID and FIELD_NAME and FIELD_DESCRIPTION) and not duplicates and not invalid,
        "taxonomy_status": "taxonomy_only",
    }
