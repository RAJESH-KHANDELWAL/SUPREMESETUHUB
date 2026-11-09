"""World catalogue."""
from .domain_registry import list_domains
WORLD_CATALOG=tuple({"world_domain_id":x["id"],"name":x["name"],"record_type":x["record_type"],"subcategory_ids":tuple(x["subcategory_ids"])} for x in list_domains())
def list_world_catalog(): return [{**x,"subcategory_ids":list(x["subcategory_ids"])} for x in WORLD_CATALOG]
def get_world_catalog_entry(domain_id): return next((x for x in list_world_catalog() if x["world_domain_id"]==domain_id),None)
