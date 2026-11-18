"""Provider identity contract for Render."""

PROVIDER_ID = "render"
PROVIDER_NAME = "Render"
PROVIDER_SCOPE = "Custom domains for services"
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
