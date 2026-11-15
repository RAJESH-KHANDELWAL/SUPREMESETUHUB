"""Independent ENGINE catalog for GLOBAL SOFTWARE."""
from .models import EngineDescriptor
PROVIDER = "GLOBAL SOFTWARE"
CHILD_ECOSYSTEMS = [
    "ADOBE SOFTWARE",
    "APPLE SOFTWARE",
    "AWS SOFTWARE",
    "GITHUB SOFTWARE",
    "GLOBAL ATLASSIAN",
    "INTEGRATIONS",
    "MICROSOFT SOFTWARE",
    "SERVICES",
    "TOOLS"
]
CATALOG = (EngineDescriptor("ENGINE-GLOBAL_SOFTWARE", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
