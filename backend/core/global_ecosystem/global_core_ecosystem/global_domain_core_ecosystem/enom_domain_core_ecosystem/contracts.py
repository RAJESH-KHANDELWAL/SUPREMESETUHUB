"""Provider identity contract for eNom."""

PROVIDER_ID = "enom"
PROVIDER_NAME = "eNom"
PROVIDER_SCOPE = "Domain reseller API"
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
