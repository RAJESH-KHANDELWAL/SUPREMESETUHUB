"""Local taxonomy binding for civil_structural_engineering under engineering_construction."""
from ..categories import FIELD_ID, FIELD_NAME, SUBCATEGORY_DEFINITIONS

SUBCATEGORY_ID = "civil_structural_engineering"
PARENT_FIELD_ID = FIELD_ID
TAXONOMY_STATUS = "taxonomy_only"

def get_subcategory_definition() -> dict:
    item = next((row for row in SUBCATEGORY_DEFINITIONS if row["id"] == SUBCATEGORY_ID), None)
    if item is None:
        raise LookupError(f"Subcategory '{SUBCATEGORY_ID}' is not registered under '{FIELD_ID}'.")
    return dict(item)

def get_api_identity() -> dict:
    item = get_subcategory_definition()
    return {"api_ecosystem_id": f"{FIELD_ID.upper()}_{SUBCATEGORY_ID.upper()}_PROFESSIONAL_SUBCATEGORY_API_ECOSYSTEM", "parent_field_id": FIELD_ID, "field_name": FIELD_NAME, "subcategory_id": SUBCATEGORY_ID, "name": item["name"], "taxonomy_status": TAXONOMY_STATUS}
