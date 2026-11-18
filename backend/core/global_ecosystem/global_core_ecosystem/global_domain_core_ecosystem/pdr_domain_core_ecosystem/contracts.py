"""Provider identity contract for Public Domain Registry."""

PROVIDER_ID = "pdr"
PROVIDER_NAME = "Public Domain Registry"
PROVIDER_SCOPE = "Registrar and reseller ecosystem"
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
