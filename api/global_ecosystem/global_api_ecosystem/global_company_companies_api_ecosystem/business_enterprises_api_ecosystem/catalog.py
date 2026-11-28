"""Curated Enterprise class metadata; not a verified profile dataset."""
from .subcategories import SUBCATEGORY_IDS
RECORD_TYPE="enterprise"
ENTITY_TYPES=tuple(SUBCATEGORY_IDS)
SUBCATEGORIES=tuple(SUBCATEGORY_IDS)
CATEGORY={"record_type":RECORD_TYPE,"name":"Enterprises","description":"Operating economic organizations; legal incorporation is not implied.","entity_types":ENTITY_TYPES,"subcategory_count":len(SUBCATEGORIES),"registry_status":"taxonomy_only"}
