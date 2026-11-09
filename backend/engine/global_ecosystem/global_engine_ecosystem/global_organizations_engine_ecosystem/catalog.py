"""Independent ENGINE catalog for GLOBAL ORGANIZATIONS."""
from .models import EngineDescriptor
PROVIDER = "GLOBAL ORGANIZATIONS"
CHILD_ECOSYSTEMS = [
    "CLASSIFICATION STANDARDS",
    "COUNTRY API ECOSYSTEMS",
    "DATA",
    "INTEGRATIONS",
    "ORGANIZATION DOMAIN API ECOSYSTEMS",
    "ORGANIZATION TYPE API ECOSYSTEMS",
    "SERVICES",
    "TESTS",
    "TOOLS"
]
CATALOG = (EngineDescriptor("ENGINE-GLOBAL_ORGANIZATIONS", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
