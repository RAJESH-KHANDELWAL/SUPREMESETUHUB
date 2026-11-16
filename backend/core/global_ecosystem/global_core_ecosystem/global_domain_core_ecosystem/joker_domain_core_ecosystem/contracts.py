"""Provider identity contract for Joker.com."""

PROVIDER_ID = "joker"
PROVIDER_NAME = "Joker.com"
PROVIDER_SCOPE = "Registrar and domain management"
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
