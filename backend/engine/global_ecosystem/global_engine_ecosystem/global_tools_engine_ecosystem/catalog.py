"""Independent ENGINE catalog for GLOBAL TOOLS."""
from .models import EngineDescriptor
PROVIDER = "GLOBAL TOOLS"
CHILD_ECOSYSTEMS = [
    "ATLASSIAN TOOLS",
    "AWS TOOLS",
    "CRAKREVENUE TOOLS",
    "EXOCLICK TOOLS",
    "GITHUB TOOLS",
    "GLOBAL TOOLS ECOSYSTEM",
    "GOOGLE TOOLS",
    "INTEGRATIONS",
    "MICROSOFT TOOLS",
    "OPENAI TOOLS",
    "SALESFORCE TOOLS",
    "SERVICES",
    "TOOLS",
    "TRAFFICJUNKY TOOLS",
    "TWILIO TOOLS"
]
CATALOG = (EngineDescriptor("ENGINE-GLOBAL_TOOLS", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
