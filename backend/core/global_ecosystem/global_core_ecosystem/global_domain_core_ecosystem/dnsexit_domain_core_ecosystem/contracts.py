"""Provider identity contract for DNSExit."""

PROVIDER_ID = "dnsexit"
PROVIDER_NAME = "DNSExit"
PROVIDER_SCOPE = "DNS and dynamic DNS"
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
