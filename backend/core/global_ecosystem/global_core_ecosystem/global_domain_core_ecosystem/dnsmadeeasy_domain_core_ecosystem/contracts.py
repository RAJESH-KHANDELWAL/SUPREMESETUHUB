"""Provider identity contract for DNS Made Easy."""

PROVIDER_ID = "dnsmadeeasy"
PROVIDER_NAME = "DNS Made Easy"
PROVIDER_SCOPE = "Managed DNS API"
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
