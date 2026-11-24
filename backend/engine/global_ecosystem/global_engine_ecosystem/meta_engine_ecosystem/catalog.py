"""Independent ENGINE catalog for META."""
from .models import EngineDescriptor
PROVIDER = "META"
CHILD_ECOSYSTEMS = [
    "META AI ECOSYSTEM",
    "META BUSINESS MANAGEMENT",
    "META FACEBOOK PAGES",
    "META GRAPH",
    "META INSTAGRAM",
    "META LOGIN IDENTITY",
    "META MARKETING ADS",
    "META MESSENGER",
    "META THREADS",
    "META WEBHOOKS",
    "META WHATSAPP BUSINESS"
]
CATALOG = (EngineDescriptor("ENGINE-META", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
