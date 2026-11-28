"""Provider identity contract for Identity Digital."""

PROVIDER_ID = "afilias"
PROVIDER_NAME = "Identity Digital"
PROVIDER_SCOPE = "Domain registry operator"
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
