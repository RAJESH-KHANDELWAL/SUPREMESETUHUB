"""Independent ENGINE catalog for GOOGLE."""
from .models import EngineDescriptor
PROVIDER = "GOOGLE"
CHILD_ECOSYSTEMS = [
    "GOOGLE ADMIN SDK",
    "GOOGLE ADS",
    "GOOGLE ANALYTICS",
    "GOOGLE BUSINESS PROFILE",
    "GOOGLE CALENDAR",
    "GOOGLE CHAT",
    "GOOGLE CLOUD",
    "GOOGLE CONTACTS",
    "GOOGLE DOCS",
    "GOOGLE DRIVE",
    "GOOGLE FIREBASE",
    "GOOGLE FORMS",
    "GOOGLE GEMINI",
    "GOOGLE GMAIL",
    "GOOGLE IDENTITY OAUTH",
    "GOOGLE MAPS PLATFORM",
    "GOOGLE MEET",
    "GOOGLE PEOPLE",
    "GOOGLE SEARCH CONSOLE",
    "GOOGLE SHEETS",
    "GOOGLE SLIDES",
    "GOOGLE VERTEX AI",
    "GOOGLE YOUTUBE"
]
CATALOG = (EngineDescriptor("ENGINE-GOOGLE", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
