"""Independent ENGINE catalog for GLOBAL VIDEO."""
from .models import EngineDescriptor
PROVIDER = "GLOBAL VIDEO"
CHILD_ECOSYSTEMS = [
    "ADOBE VIDEO",
    "AWS VIDEO",
    "BANGBROS VIDEO",
    "BRAZZERS VIDEO",
    "CLIPS4SALE VIDEO",
    "EVILANGEL VIDEO",
    "FANSLY VIDEO",
    "FAPHOUSE VIDEO",
    "GOOGLE VIDEO",
    "INTEGRATIONS",
    "LOYALFANS VIDEO",
    "MANYVIDS VIDEO",
    "NAUGHTYAMERICA VIDEO",
    "NVIDIA VIDEO",
    "ONLYFANS VIDEO",
    "PORNHUB VIDEO",
    "REALITYKINGS VIDEO",
    "SERVICES",
    "TOOLS",
    "XHAMSTER VIDEO",
    "XVIDEOS VIDEO",
    "ZOOM VIDEO"
]
CATALOG = (EngineDescriptor("ENGINE-GLOBAL_VIDEO", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
