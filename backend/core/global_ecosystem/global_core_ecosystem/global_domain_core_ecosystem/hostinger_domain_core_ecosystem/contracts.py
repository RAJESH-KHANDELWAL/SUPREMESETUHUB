"""Provider identity contract for Hostinger."""

PROVIDER_ID = "hostinger"
PROVIDER_NAME = "Hostinger"
PROVIDER_SCOPE = "Domain management and DNS"
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
