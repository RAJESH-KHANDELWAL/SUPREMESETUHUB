"""Provider identity contract for DuckDNS."""

PROVIDER_ID = "duckdns"
PROVIDER_NAME = "DuckDNS"
PROVIDER_SCOPE = "Dynamic DNS service"
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
