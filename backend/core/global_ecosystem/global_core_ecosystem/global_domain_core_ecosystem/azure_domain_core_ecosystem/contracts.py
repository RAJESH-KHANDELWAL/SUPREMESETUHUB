"""Provider identity contract for Microsoft Azure DNS."""

PROVIDER_ID = "azure"
PROVIDER_NAME = "Microsoft Azure DNS"
PROVIDER_SCOPE = "DNS zones and records"
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
