"""Provider identity contract for Fly.io."""

PROVIDER_ID = "flyio"
PROVIDER_NAME = "Fly.io"
PROVIDER_SCOPE = "Application domain and certificate management"
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
