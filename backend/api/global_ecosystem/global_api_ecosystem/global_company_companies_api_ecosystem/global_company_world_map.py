"""Crosswalk for the three Company Companies record classes."""
from .classification_registry import list_record_classes
GLOBAL_COMPANY_WORLD_MAP=tuple({"world_domain_id":"global-"+x["record_type"].replace("_","-"),"record_type":x["record_type"],"module":x["module"]} for x in list_record_classes())
def list_world_domains(): return [dict(x) for x in GLOBAL_COMPANY_WORLD_MAP]
def get_world_domain(domain_id): return next((dict(x) for x in GLOBAL_COMPANY_WORLD_MAP if x["world_domain_id"]==domain_id),None)
