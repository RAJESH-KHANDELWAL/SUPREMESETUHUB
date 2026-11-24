"""Independent ENGINE catalog for ATLASSIAN."""
from .models import EngineDescriptor
PROVIDER = "ATLASSIAN"
CHILD_ECOSYSTEMS = [
    "ATLASSIAN ADMIN IDENTITY",
    "ATLASSIAN BITBUCKET",
    "ATLASSIAN CONFLUENCE",
    "ATLASSIAN JIRA",
    "ATLASSIAN JIRA SERVICE MANAGEMENT"
]
CATALOG = (EngineDescriptor("ENGINE-ATLASSIAN", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
