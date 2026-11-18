"""Provider identity contract for Hetzner."""

PROVIDER_ID = "hetzner"
PROVIDER_NAME = "Hetzner"
PROVIDER_SCOPE = "DNS and infrastructure services"
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
