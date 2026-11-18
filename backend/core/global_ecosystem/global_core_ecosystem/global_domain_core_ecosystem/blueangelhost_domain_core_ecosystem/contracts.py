"""Provider identity contract for BlueAngelHost."""

PROVIDER_ID = "blueangelhost"
PROVIDER_NAME = "BlueAngelHost"
PROVIDER_SCOPE = "Hosting provider reference; domain services/API capabilities require verification"
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
