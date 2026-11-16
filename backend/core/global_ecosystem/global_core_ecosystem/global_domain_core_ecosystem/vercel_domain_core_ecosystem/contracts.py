"""Provider identity contract for Vercel."""

PROVIDER_ID = "vercel"
PROVIDER_NAME = "Vercel"
PROVIDER_SCOPE = "Project domain configuration"
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
