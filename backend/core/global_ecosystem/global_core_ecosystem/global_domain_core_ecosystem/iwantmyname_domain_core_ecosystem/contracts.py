"""Provider identity contract for iwantmyname."""

PROVIDER_ID = "iwantmyname"
PROVIDER_NAME = "iwantmyname"
PROVIDER_SCOPE = "Domain registration and DNS"
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
