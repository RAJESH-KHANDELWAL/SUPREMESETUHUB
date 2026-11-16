"""Provider identity contract for Hurricane Electric DNS."""

PROVIDER_ID = "he"
PROVIDER_NAME = "Hurricane Electric DNS"
PROVIDER_SCOPE = "Authoritative DNS service"
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
