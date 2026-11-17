"""Addressable API Ecosystem descriptor for this professional subcategory."""
from . import SUBCATEGORY_ID, PARENT_FIELD_ID, TAXONOMY_STATUS
from ..categories import SUBCATEGORY_DEFINITIONS

def get_api_ecosystem() -> dict:
    item = next((row for row in SUBCATEGORY_DEFINITIONS if row["id"] == SUBCATEGORY_ID), None)
    if item is None:
        raise LookupError(f"Unknown professional subcategory: {SUBCATEGORY_ID}")
    return {"api_ecosystem_id": f"{PARENT_FIELD_ID.upper()}_{SUBCATEGORY_ID.upper()}_PROFESSIONAL_SUBCATEGORY_API_ECOSYSTEM", "api_ecosystem_name": f'{item["name"]} API Ecosystem', "parent_api_ecosystem_id": f"{PARENT_FIELD_ID.upper()}_PROFESSIONAL_FIELD_API_ECOSYSTEM", "parent_field_id": PARENT_FIELD_ID, "subcategory_id": SUBCATEGORY_ID, "name": item["name"], "description": item["description"], "taxonomy_status": TAXONOMY_STATUS, "capabilities": ["status", "detail", "validation"], "verification": {"vacancy_verified": False, "employer_verified": False, "credential_verified": False}}
