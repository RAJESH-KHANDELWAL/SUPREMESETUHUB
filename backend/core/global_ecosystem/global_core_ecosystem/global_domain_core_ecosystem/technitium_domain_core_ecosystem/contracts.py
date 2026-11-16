"""Provider identity contract for Technitium DNS Server."""

PROVIDER_ID = "technitium"
PROVIDER_NAME = "Technitium DNS Server"
PROVIDER_SCOPE = "DNS server API"
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
