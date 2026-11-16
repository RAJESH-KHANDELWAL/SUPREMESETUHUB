"""Provider identity contract for Internet.bs."""

PROVIDER_ID = "internetbs"
PROVIDER_NAME = "Internet.bs"
PROVIDER_SCOPE = "Domain registration API"
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
