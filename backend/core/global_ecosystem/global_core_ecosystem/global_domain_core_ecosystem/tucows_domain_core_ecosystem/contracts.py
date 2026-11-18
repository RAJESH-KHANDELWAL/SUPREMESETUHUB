"""Provider identity contract for Tucows."""

PROVIDER_ID = "tucows"
PROVIDER_NAME = "Tucows"
PROVIDER_SCOPE = "Domain registrar and reseller ecosystem"
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
