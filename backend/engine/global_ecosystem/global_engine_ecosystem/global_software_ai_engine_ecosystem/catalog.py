"""Independent category catalog for GLOBAL SOFTWARE AI ENGINE ECOSYSTEM."""
from .models import EngineDescriptor
CATEGORY = "SOFTWARE_AI"
CATALOG = (EngineDescriptor("GLOBAL-SOFTWARE-AI-ENGINE-ECOSYSTEM", "GLOBAL SOFTWARE AI ENGINE ECOSYSTEM", ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines(): return [dict(engine_id=x.engine_id,name=x.name,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
