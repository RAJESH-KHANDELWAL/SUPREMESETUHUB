"""Provider identity contract for Constellix."""

PROVIDER_ID = "constellix"
PROVIDER_NAME = "Constellix"
PROVIDER_SCOPE = "Managed DNS API"
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
