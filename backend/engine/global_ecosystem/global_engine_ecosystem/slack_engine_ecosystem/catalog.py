"""Independent ENGINE catalog for SLACK."""
from .models import EngineDescriptor
PROVIDER = "SLACK"
CHILD_ECOSYSTEMS = [
    "SLACK ADMIN",
    "SLACK BOOKMARKS",
    "SLACK CANVASES",
    "SLACK CONVERSATIONS",
    "SLACK EVENTS",
    "SLACK FILES",
    "SLACK LISTS",
    "SLACK MESSAGES",
    "SLACK OAUTH",
    "SLACK REACTIONS",
    "SLACK SEARCH",
    "SLACK USERS",
    "SLACK WEBHOOKS",
    "SLACK WORKFLOW"
]
CATALOG = (EngineDescriptor("ENGINE-SLACK", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
