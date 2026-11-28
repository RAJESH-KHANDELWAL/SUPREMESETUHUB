"""Independent ENGINE catalog for DIGITALOCEAN."""
from .models import EngineDescriptor
PROVIDER = "DIGITALOCEAN"
CHILD_ECOSYSTEMS = [
    "DIGITALOCEAN CLOUD",
    "DIGITALOCEAN HOSTING",
    "DIGITALOCEAN SERVER",
    "DIGITALOCEAN STORAGE",
    "DIGITALOCEAN VPS"
]
CATALOG = (EngineDescriptor("ENGINE-DIGITALOCEAN", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
