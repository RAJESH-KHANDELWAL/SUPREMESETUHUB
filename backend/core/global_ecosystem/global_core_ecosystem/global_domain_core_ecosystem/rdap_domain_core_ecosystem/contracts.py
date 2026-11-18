"""Provider identity contract for RDAP."""

PROVIDER_ID = "rdap"
PROVIDER_NAME = "RDAP"
PROVIDER_SCOPE = "Standard domain registration data protocol"
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
