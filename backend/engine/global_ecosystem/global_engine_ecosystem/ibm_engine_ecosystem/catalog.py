"""Independent ENGINE catalog for IBM."""
from .models import EngineDescriptor
PROVIDER = "IBM"
CHILD_ECOSYSTEMS = [
    "IBM API CONNECT GATEWAY",
    "IBM BILLING USAGE COST",
    "IBM CLOUD OBJECT STORAGE",
    "IBM CLOUD PLATFORM",
    "IBM CLOUDANT",
    "IBM CODE ENGINE SERVERLESS",
    "IBM DB2 DATABASE",
    "IBM IAM IDENTITY",
    "IBM KUBERNETES CONTAINERS",
    "IBM MONITORING ACTIVITY TRACKER",
    "IBM RESOURCE CONTROLLER CATALOG",
    "IBM SECRETS MANAGER",
    "IBM SECURITY KEY PROTECT",
    "IBM VPC COMPUTE NETWORKING",
    "IBM WATSONX AI",
    "IBM WATSONX DATA"
]
CATALOG = (EngineDescriptor("ENGINE-IBM", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
