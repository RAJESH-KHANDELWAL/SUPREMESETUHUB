"""Independent ENGINE catalog for ADOBE."""
from .models import EngineDescriptor
PROVIDER = "ADOBE"
CHILD_ECOSYSTEMS = [
    "ADOBE ACROBAT SIGN",
    "ADOBE COMMERCE",
    "ADOBE CREATIVE CLOUD ASSETS",
    "ADOBE EXPERIENCE PLATFORM",
    "ADOBE FIREFLY SERVICES",
    "ADOBE OAUTH IDENTITY ECOSYSTEM",
    "ADOBE PDF SERVICES",
    "ADOBE VIDEO FRAMEIO"
]
CATALOG = (EngineDescriptor("ENGINE-ADOBE", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
