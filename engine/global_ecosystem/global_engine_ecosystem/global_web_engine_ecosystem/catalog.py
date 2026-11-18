"""Independent ENGINE catalog for GLOBAL WEB."""
from .models import EngineDescriptor
PROVIDER = "GLOBAL WEB"
CHILD_ECOSYSTEMS = [
    "AWS WEB",
    "CLOUDFLARE WEB",
    "GOOGLE WEB",
    "INTEGRATIONS",
    "MICROSOFT WEB",
    "SERVICES",
    "TOOLS"
]
CATALOG = (EngineDescriptor("ENGINE-GLOBAL_WEB", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
