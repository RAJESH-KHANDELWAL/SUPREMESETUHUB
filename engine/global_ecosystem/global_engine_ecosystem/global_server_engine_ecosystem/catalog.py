"""ENGINE-owned catalog for GLOBAL SERVER execution units."""
from .models import EngineDescriptor

PROVIDER = "GLOBAL SERVER"
CHILD_ECOSYSTEMS = (
    "ABELOHOST SERVER", "AWS SERVER", "CLOUDFLARE SERVER",
    "DIGITALOCEAN SERVER", "GOOGLE SERVER", "INTEGRATIONS",
    "MICROSOFT SERVER", "SERVICES", "TOOLS", "VICETEMPLE SERVER",
)
CATALOG = (
    EngineDescriptor(
        engine_id="ENGINE-GLOBAL-SERVER",
        name=PROVIDER,
        provider=PROVIDER,
        capabilities=("LIFECYCLE", "EXECUTION_BOUNDARY", "PROVIDER_ADAPTERS"),
    ),
)

def list_engines():
    return [{
        "engine_id": item.engine_id,
        "name": item.name,
        "provider": item.provider,
        "capabilities": list(item.capabilities),
        "metadata": dict(item.metadata),
    } for item in CATALOG]
