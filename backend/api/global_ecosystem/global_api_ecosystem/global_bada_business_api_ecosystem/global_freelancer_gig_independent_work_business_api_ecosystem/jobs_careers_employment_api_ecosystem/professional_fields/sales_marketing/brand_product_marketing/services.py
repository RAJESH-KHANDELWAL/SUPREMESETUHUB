"""Service operations for this professional subcategory taxonomy package."""
from . import SUBCATEGORY_ID, PARENT_FIELD_ID
from .api_ecosystem import get_api_ecosystem
from .models import ProfessionalSubcategory
from ..categories import SUBCATEGORY_DEFINITIONS
from .validators import validate_subcategory
def get_subcategory() -> ProfessionalSubcategory:
    item = next((row for row in SUBCATEGORY_DEFINITIONS if row["id"] == SUBCATEGORY_ID), None)
    if item is None:
        raise LookupError(f"Unknown professional subcategory: {SUBCATEGORY_ID}")
    return ProfessionalSubcategory(id=item["id"], name=item["name"], description=item["description"], parent_field_id=PARENT_FIELD_ID)
def get_status() -> dict:
    ecosystem = get_api_ecosystem()
    record = {"id": ecosystem["subcategory_id"], "name": ecosystem["name"], "description": ecosystem["description"], "parent_field_id": ecosystem["parent_field_id"]}
    return {"success": True, "api_ecosystem": ecosystem, "integrity": validate_subcategory(record)}
