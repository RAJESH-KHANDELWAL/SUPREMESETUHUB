"""Provider identity contract for IONOS."""

PROVIDER_ID = "ionos"
PROVIDER_NAME = "IONOS"
PROVIDER_SCOPE = "Domain and DNS management"
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
