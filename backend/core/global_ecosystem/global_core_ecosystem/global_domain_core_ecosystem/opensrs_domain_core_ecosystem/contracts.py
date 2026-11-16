"""Provider identity contract for OpenSRS."""

PROVIDER_ID = "opensrs"
PROVIDER_NAME = "OpenSRS"
PROVIDER_SCOPE = "Domain reseller and registrar API"
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
