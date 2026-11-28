"""Independent category catalog for GLOBAL FREELANCER ENGINE ECOSYSTEM."""
from .models import EngineDescriptor
CATEGORY = "FREELANCER"
CATALOG = (EngineDescriptor("GLOBAL-FREELANCER-ENGINE-ECOSYSTEM", "GLOBAL FREELANCER ENGINE ECOSYSTEM", ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines(): return [dict(engine_id=x.engine_id,name=x.name,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
