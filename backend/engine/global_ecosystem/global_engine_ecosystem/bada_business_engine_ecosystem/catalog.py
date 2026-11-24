"""Independent ENGINE catalog for BADA BUSINESS."""
from .models import EngineDescriptor
PROVIDER = "BADA BUSINESS"
CHILD_ECOSYSTEMS = [
    "PROGRAMS"
]
CATALOG = (EngineDescriptor("ENGINE-BADA_BUSINESS", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
