"""Independent ENGINE catalog for GLOBAL SERVER."""
from .models import EngineDescriptor
PROVIDER = "GLOBAL SERVER"
CHILD_ECOSYSTEMS = [
    "ABELOHOST SERVER",
    "AWS SERVER",
    "CLOUDFLARE SERVER",
    "DIGITALOCEAN SERVER",
    "GOOGLE SERVER",
    "INTEGRATIONS",
    "MICROSOFT SERVER",
    "SERVICES",
    "TOOLS",
    "VICETEMPLE SERVER"
]
CATALOG = (EngineDescriptor("ENGINE-GLOBAL_SERVER", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
