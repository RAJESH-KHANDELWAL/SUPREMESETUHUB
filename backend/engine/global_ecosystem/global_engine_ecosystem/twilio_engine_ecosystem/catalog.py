"""Independent ENGINE catalog for TWILIO."""
from .models import EngineDescriptor
PROVIDER = "TWILIO"
CHILD_ECOSYSTEMS = []
CATALOG = (EngineDescriptor("ENGINE-TWILIO", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
