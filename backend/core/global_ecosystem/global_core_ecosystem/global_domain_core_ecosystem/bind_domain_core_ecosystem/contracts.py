"""Provider identity contract for ISC BIND."""

PROVIDER_ID = "bind"
PROVIDER_NAME = "ISC BIND"
PROVIDER_SCOPE = "DNS server software and management"
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
