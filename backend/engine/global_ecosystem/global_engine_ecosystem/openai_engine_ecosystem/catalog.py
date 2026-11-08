"""Independent ENGINE catalog for OPENAI."""
from .models import EngineDescriptor
PROVIDER = "OPENAI"
CHILD_ECOSYSTEMS = [
    "OPENAI AGENTS",
    "OPENAI AGENTS SDK",
    "OPENAI APPS SDK",
    "OPENAI CHATGPT",
    "OPENAI CHATGPT BUSINESS",
    "OPENAI CHATGPT EDUCATION",
    "OPENAI CHATGPT ENTERPRISE",
    "OPENAI CHATGPT HEALTH",
    "OPENAI CHATKIT",
    "OPENAI CODEX",
    "OPENAI DOTS",
    "OPENAI PLUGINS MCP",
    "OPENAI SDK LIBRARIES",
    "OPENAI SORA"
]
CATALOG = (EngineDescriptor("ENGINE-OPENAI", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
