"""Independent category catalog for GLOBAL COMPANIES ENGINE ECOSYSTEM."""
from .models import EngineDescriptor
CATEGORY = "COMPANIES"
CATALOG = (EngineDescriptor("GLOBAL-COMPANIES-ENGINE-ECOSYSTEM", "GLOBAL COMPANIES ENGINE ECOSYSTEM", ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines(): return [dict(engine_id=x.engine_id,name=x.name,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
