"""Independent ENGINE catalog for GLOBAL WEBSITE."""
from .models import EngineDescriptor
PROVIDER = "GLOBAL WEBSITE"
CHILD_ECOSYSTEMS = [
    "AWS WEBSITE",
    "GOOGLE WEBSITE",
    "INTEGRATIONS",
    "MICROSOFT WEBSITE",
    "SERVICES",
    "TOOLS",
    "VICETEMPLE WEBSITE"
]
CATALOG = (EngineDescriptor("ENGINE-GLOBAL_WEBSITE", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
