"""Curated business class metadata; not a verified profile dataset."""
from .subcategories import SUBCATEGORY_IDS
RECORD_TYPE = "business"
ENTITY_TYPES = tuple(SUBCATEGORY_IDS)
SUBCATEGORIES = tuple(SUBCATEGORY_IDS)
CATEGORY = {"record_type": RECORD_TYPE, "name": "Businesses", "description": "Operating businesses that may or may not be represented as a separately registered legal entity, including sole proprietors, MSMEs, startups and franchises.", "entity_types": ENTITY_TYPES, "subcategory_count": len(SUBCATEGORIES), "registry_status": "taxonomy_only"}
