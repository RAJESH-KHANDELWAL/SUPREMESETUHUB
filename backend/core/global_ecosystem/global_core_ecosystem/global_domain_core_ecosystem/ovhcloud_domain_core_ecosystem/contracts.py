"""Provider identity contract for OVHcloud."""

PROVIDER_ID = "ovhcloud"
PROVIDER_NAME = "OVHcloud"
PROVIDER_SCOPE = "Domain and DNS management APIs"
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
