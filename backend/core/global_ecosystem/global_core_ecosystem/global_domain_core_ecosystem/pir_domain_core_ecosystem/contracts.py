"""Provider identity contract for Public Interest Registry."""

PROVIDER_ID = "pir"
PROVIDER_NAME = "Public Interest Registry"
PROVIDER_SCOPE = ".org domain registry"
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
