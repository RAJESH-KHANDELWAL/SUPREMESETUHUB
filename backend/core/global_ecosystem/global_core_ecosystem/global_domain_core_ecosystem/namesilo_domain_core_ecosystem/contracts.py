"""Provider identity contract for NameSilo."""

PROVIDER_ID = "namesilo"
PROVIDER_NAME = "NameSilo"
PROVIDER_SCOPE = "Domain registrar API"
STATUS = "CORE_CATALOG_ONLY"
LIVE_CONNECTION_VERIFIED = False
API_AVAILABLE = None


def readiness():
    return {
        "provider_id": PROVIDER_ID,
        "status": STATUS,
        "live_connection_verified": False,
        "execution_enabled": False,
    }
