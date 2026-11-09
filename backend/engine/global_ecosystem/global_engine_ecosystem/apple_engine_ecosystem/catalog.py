"""Independent ENGINE catalog for APPLE."""
from .models import EngineDescriptor
PROVIDER = "APPLE"
CHILD_ECOSYSTEMS = [
    "APPLE APP STORE CONNECT",
    "APPLE APP STORE SERVER",
    "APPLE DEVICE MANAGEMENT",
    "APPLE ICLOUD CLOUDKIT",
    "APPLE PAY",
    "APPLE PUSH NOTIFICATION",
    "APPLE SIGN IN WITH APPLE",
    "APPLE STOREKIT"
]
CATALOG = (EngineDescriptor("ENGINE-APPLE", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
