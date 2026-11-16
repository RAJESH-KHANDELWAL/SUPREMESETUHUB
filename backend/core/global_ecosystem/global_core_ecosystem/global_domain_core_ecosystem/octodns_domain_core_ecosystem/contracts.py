"""Provider identity contract for octoDNS."""

PROVIDER_ID = "octodns"
PROVIDER_NAME = "octoDNS"
PROVIDER_SCOPE = "DNS management automation tool"
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
