from .catalog import MODULES
REGISTRY={}
for item in MODULES:
    if item["module_id"] in REGISTRY: raise ValueError("Duplicate module ID: "+item["module_id"])
    REGISTRY[item["module_id"]]=item["directory"]
def resolve(module_id): return REGISTRY.get(module_id.strip().upper())
def list_ids(): return sorted(REGISTRY)
