"""Independent ENGINE catalog for DEEPSEEK."""
from .models import EngineDescriptor
PROVIDER = "DEEPSEEK"
CHILD_ECOSYSTEMS = [
    "DEEPSEEK CHAT COMPLETIONS",
    "DEEPSEEK FETCH",
    "DEEPSEEK RESPONSES",
    "DEEPSEEK SEARCH"
]
CATALOG = (EngineDescriptor("ENGINE-DEEPSEEK", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
