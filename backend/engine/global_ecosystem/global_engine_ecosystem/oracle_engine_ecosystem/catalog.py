"""Independent ENGINE catalog for ORACLE."""
from .models import EngineDescriptor
PROVIDER = "ORACLE"
CHILD_ECOSYSTEMS = [
    "ORACLE AI SERVICES",
    "ORACLE AUTONOMOUS DATABASE",
    "ORACLE BASE DATABASE",
    "ORACLE BLOCK VOLUMES",
    "ORACLE COMPUTE",
    "ORACLE COMPUTE INSTANCES",
    "ORACLE DATA SCIENCE",
    "ORACLE DATABASE TOOLS",
    "ORACLE ENTERPRISE APPLICATIONS",
    "ORACLE FUSION CLOUD APPLICATIONS",
    "ORACLE GENERATIVE AI",
    "ORACLE IDENTITY",
    "ORACLE MYSQL HEATWAVE",
    "ORACLE NETWORKING",
    "ORACLE OBJECT STORAGE",
    "ORACLE OBSERVABILITY",
    "ORACLE VIRTUAL CLOUD NETWORKS",
    "TESTS"
]
CATALOG = (EngineDescriptor("ENGINE-ORACLE", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
