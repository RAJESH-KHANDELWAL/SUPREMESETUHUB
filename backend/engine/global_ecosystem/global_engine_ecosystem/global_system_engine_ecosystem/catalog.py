"""Independent ENGINE catalog for GLOBAL SYSTEM."""
from .models import EngineDescriptor
PROVIDER = "GLOBAL SYSTEM"
CHILD_ECOSYSTEMS = [
    "APPLE SYSTEM",
    "INTEGRATIONS",
    "SERVICES",
    "TOOLS"
]
CATALOG = (EngineDescriptor("ENGINE-GLOBAL_SYSTEM", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
