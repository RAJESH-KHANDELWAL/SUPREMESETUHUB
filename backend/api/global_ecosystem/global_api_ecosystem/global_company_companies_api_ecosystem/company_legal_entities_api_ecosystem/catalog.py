"""Curated company class metadata; not a verified profile dataset."""
from .subcategories import SUBCATEGORY_IDS
RECORD_TYPE = "company"
ENTITY_TYPES = tuple(SUBCATEGORY_IDS)
SUBCATEGORIES = tuple(SUBCATEGORY_IDS)
CATEGORY = {"record_type": RECORD_TYPE, "name": "Companies", "description": "Registered legal entities and formally constituted organizations.", "entity_types": ENTITY_TYPES, "subcategory_count": len(SUBCATEGORIES), "registry_status": "taxonomy_only"}
