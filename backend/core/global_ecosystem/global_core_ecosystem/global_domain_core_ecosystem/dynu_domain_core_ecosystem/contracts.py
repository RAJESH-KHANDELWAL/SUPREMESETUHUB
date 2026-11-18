"""Provider identity contract for Dynu."""

PROVIDER_ID = "dynu"
PROVIDER_NAME = "Dynu"
PROVIDER_SCOPE = "Dynamic DNS and domain services"
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
