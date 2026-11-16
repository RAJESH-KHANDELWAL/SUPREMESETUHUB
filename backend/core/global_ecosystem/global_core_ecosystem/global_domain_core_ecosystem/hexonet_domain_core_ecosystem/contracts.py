"""Provider identity contract for HEXONET."""

PROVIDER_ID = "hexonet"
PROVIDER_NAME = "HEXONET"
PROVIDER_SCOPE = "Domain reseller API"
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
