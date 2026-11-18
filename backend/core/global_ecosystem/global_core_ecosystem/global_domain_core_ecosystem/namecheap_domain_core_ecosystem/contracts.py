"""Provider identity contract for Namecheap."""

PROVIDER_ID = "namecheap"
PROVIDER_NAME = "Namecheap"
PROVIDER_SCOPE = "Domain registration, DNS, SSL"
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
