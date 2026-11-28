"""Independent ENGINE catalog for SALESFORCE."""
from .models import EngineDescriptor
PROVIDER = "SALESFORCE"
CHILD_ECOSYSTEMS = [
    "SALESFORCE ANALYTICS",
    "SALESFORCE APEX",
    "SALESFORCE BULK",
    "SALESFORCE COMPOSITE",
    "SALESFORCE DATA CLOUD",
    "SALESFORCE FILES CONTENT",
    "SALESFORCE IDENTITY OAUTH",
    "SALESFORCE MARKETING CLOUD",
    "SALESFORCE METADATA TOOLING",
    "SALESFORCE PLATFORM EVENTS PUBSUB",
    "SALESFORCE REST",
    "SALESFORCE SERVICE CLOUD",
    "SALESFORCE SOAP",
    "SALESFORCE STREAMING"
]
CATALOG = (EngineDescriptor("ENGINE-SALESFORCE", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
