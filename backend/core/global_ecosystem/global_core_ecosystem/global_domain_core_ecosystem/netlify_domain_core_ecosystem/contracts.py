"""Provider identity contract for Netlify."""

PROVIDER_ID = "netlify"
PROVIDER_NAME = "Netlify"
PROVIDER_SCOPE = "Custom domain management"
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
