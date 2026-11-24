"""Compatibility subcategory accessor for the canonical finance ecosystem."""
from . import DOMAIN_ID, SUBCATEGORY_IDS

def list_subcategories():
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]

__all__ = ["SUBCATEGORY_IDS", "list_subcategories"]
