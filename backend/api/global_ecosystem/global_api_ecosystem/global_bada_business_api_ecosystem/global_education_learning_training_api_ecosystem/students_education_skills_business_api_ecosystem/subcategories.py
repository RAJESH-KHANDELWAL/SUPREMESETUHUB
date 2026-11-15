"""Subcategory accessors for the students_education_skills domain package."""
from . import DOMAIN_ID, SUBCATEGORY_IDS

def list_subcategories():
    """Return stable IDs and presentation labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]

__all__ = ["SUBCATEGORY_IDS", "list_subcategories"]
