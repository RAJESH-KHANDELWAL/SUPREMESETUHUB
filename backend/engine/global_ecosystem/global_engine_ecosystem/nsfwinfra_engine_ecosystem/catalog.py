"""Independent ENGINE catalog for NSFWINFRA."""
from .models import EngineDescriptor
PROVIDER = "NSFWINFRA"
CHILD_ECOSYSTEMS = [
    "NSFWINFRA ACCOUNT LIMITS",
    "NSFWINFRA ANIME GENERATION",
    "NSFWINFRA ASYNC JOBS",
    "NSFWINFRA IMAGE EDITING",
    "NSFWINFRA IMAGE GENERATION",
    "NSFWINFRA IMAGE TO VIDEO",
    "NSFWINFRA IMAGE VIDEO EFFECTS",
    "NSFWINFRA SIGNED UPLOADS",
    "NSFWINFRA TEXT TO VIDEO",
    "NSFWINFRA WEBHOOKS"
]
CATALOG = (EngineDescriptor("ENGINE-NSFWINFRA", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
