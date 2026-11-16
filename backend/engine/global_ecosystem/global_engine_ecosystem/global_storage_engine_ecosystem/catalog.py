"""Independent ENGINE catalog for GLOBAL STORAGE."""
from .models import EngineDescriptor
PROVIDER = "GLOBAL STORAGE"
CHILD_ECOSYSTEMS = [
    "APPLE STORAGE",
    "AWS STORAGE",
    "DIGITALOCEAN STORAGE",
    "GOOGLE STORAGE",
    "INTEGRATIONS",
    "MICROSOFT STORAGE",
    "SERVICES",
    "TOOLS"
]
CATALOG = (EngineDescriptor("ENGINE-GLOBAL_STORAGE", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
