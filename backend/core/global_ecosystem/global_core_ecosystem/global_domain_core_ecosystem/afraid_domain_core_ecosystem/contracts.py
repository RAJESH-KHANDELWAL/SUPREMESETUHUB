"""Provider identity contract for FreeDNS afraid.org."""

PROVIDER_ID = "afraid"
PROVIDER_NAME = "FreeDNS afraid.org"
PROVIDER_SCOPE = "Dynamic DNS and DNS hosting"
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
