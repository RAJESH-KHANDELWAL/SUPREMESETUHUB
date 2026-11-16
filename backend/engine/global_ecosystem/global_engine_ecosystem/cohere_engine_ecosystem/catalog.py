"""Independent ENGINE catalog for COHERE."""
from .models import EngineDescriptor
PROVIDER = "COHERE"
CHILD_ECOSYSTEMS = [
    "COHERE CLASSIFY",
    "COHERE COMMAND",
    "COHERE EMBED",
    "COHERE RERANK",
    "COHERE TOKENIZE"
]
CATALOG = (EngineDescriptor("ENGINE-COHERE", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
