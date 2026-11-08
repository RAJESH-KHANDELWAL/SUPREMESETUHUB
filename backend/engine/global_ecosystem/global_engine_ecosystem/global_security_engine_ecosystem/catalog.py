"""Independent ENGINE catalog for GLOBAL SECURITY."""
from .models import EngineDescriptor
PROVIDER = "GLOBAL SECURITY"
CHILD_ECOSYSTEMS = [
    "APPLE SECURITY",
    "AWS SECURITY",
    "CLOUDFLARE SECURITY",
    "GOOGLE SECURITY",
    "IBM SECURITY",
    "INTEGRATIONS",
    "MICROSOFT SECURITY",
    "SERVICES",
    "TOOLS"
]
CATALOG = (EngineDescriptor("ENGINE-GLOBAL_SECURITY", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
