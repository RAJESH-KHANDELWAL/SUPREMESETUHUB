"""Independent ENGINE catalog for MISTRAL."""
from .models import EngineDescriptor
PROVIDER = "MISTRAL"
CHILD_ECOSYSTEMS = [
    "MISTRAL AGENTS",
    "MISTRAL AUDIO",
    "MISTRAL BATCH",
    "MISTRAL CHAT",
    "MISTRAL EMBEDDINGS",
    "MISTRAL FIM COMPLETIONS",
    "MISTRAL FINE TUNING",
    "MISTRAL MODELS",
    "MISTRAL OCR"
]
CATALOG = (EngineDescriptor("ENGINE-MISTRAL", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
