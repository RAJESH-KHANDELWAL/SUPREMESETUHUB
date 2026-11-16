"""Curated freelancer class metadata; not a verified profile dataset."""
from .subcategories import SUBCATEGORY_IDS
RECORD_TYPE = "freelancer"
ENTITY_TYPES = tuple(SUBCATEGORY_IDS)
SUBCATEGORIES = tuple(SUBCATEGORY_IDS)
CATEGORY = {"record_type": RECORD_TYPE, "name": "Freelancers", "description": "Independent individual professionals, self-employed specialists and individual service providers.", "entity_types": ENTITY_TYPES, "subcategory_count": len(SUBCATEGORIES), "registry_status": "taxonomy_only"}
