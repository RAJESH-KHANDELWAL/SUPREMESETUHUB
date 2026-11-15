"""Independent ENGINE catalog for ANTHROPIC."""
from .models import EngineDescriptor
PROVIDER = "ANTHROPIC"
CHILD_ECOSYSTEMS = [
    "ANTHROPIC ADMIN WORKSPACES",
    "ANTHROPIC AUTH IDENTITY ECOSYSTEM",
    "ANTHROPIC BATCHES",
    "ANTHROPIC FILES",
    "ANTHROPIC MANAGED AGENTS",
    "ANTHROPIC MESSAGES",
    "ANTHROPIC MODELS",
    "ANTHROPIC TOKEN COUNTING",
    "ANTHROPIC TOOL USE"
]
CATALOG = (EngineDescriptor("ENGINE-ANTHROPIC", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
