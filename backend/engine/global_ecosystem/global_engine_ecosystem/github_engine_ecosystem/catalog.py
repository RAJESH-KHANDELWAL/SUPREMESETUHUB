"""Independent ENGINE catalog for GITHUB."""
from .models import EngineDescriptor
PROVIDER = "GITHUB"
CHILD_ECOSYSTEMS = [
    "GITHUB ACTIONS",
    "GITHUB APPS",
    "GITHUB AUTHENTICATION",
    "GITHUB CHECKS",
    "GITHUB GRAPHQL",
    "GITHUB ISSUES",
    "GITHUB ORGANIZATIONS",
    "GITHUB PULL REQUESTS",
    "GITHUB REPOSITORIES",
    "GITHUB REST",
    "GITHUB SECURITY",
    "GITHUB WEBHOOKS"
]
CATALOG = (EngineDescriptor("ENGINE-GITHUB", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
