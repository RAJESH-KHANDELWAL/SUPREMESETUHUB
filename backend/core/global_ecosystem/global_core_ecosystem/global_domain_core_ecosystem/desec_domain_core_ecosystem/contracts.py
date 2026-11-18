"""Provider identity contract for deSEC DNS."""

PROVIDER_ID = "desec"
PROVIDER_NAME = "deSEC DNS"
PROVIDER_SCOPE = "DNS hosting service"
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
