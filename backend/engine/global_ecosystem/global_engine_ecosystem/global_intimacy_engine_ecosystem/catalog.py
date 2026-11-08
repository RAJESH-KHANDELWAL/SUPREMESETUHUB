"""Independent category catalog for GLOBAL INTIMACY ENGINE ECOSYSTEM."""
from .models import EngineDescriptor
CATEGORY = "INTIMACY"
CATALOG = (EngineDescriptor("GLOBAL-INTIMACY-ENGINE-ECOSYSTEM", "GLOBAL INTIMACY ENGINE ECOSYSTEM", ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines(): return [dict(engine_id=x.engine_id,name=x.name,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
