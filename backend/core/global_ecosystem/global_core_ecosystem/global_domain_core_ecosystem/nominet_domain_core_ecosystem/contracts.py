"""Provider identity contract for Nominet."""

PROVIDER_ID = "nominet"
PROVIDER_NAME = "Nominet"
PROVIDER_SCOPE = "UK .uk domain registry"
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
