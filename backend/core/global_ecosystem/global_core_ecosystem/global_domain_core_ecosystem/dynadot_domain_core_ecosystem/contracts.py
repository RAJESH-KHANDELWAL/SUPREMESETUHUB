"""Provider identity contract for Dynadot."""

PROVIDER_ID = "dynadot"
PROVIDER_NAME = "Dynadot"
PROVIDER_SCOPE = "Domain registration and DNS API"
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
