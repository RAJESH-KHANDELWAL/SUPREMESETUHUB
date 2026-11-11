"""Non-invasive readiness reporting; does not claim live connectivity."""
from .catalog import ANTHROPIC_CAPABILITIES
from .constants import PROVIDER_ID, STATUS_CATALOG_ONLY

def readiness_report() -> dict:
    return {
        "provider_id": PROVIDER_ID, "status": STATUS_CATALOG_ONLY,
        "live_connection_verified": False, "credential_configured": None,
        "engine_registered": None, "database_persistence": None,
        "capability_count": len(ANTHROPIC_CAPABILITIES),
        "notes": [
            "This domain package provides catalog and request planning only.",
            "API transport, credential storage, authorization, persistence, and execution belong to separate layers.",
            "A separate integration test is required before reporting live readiness.",
        ],
    }
