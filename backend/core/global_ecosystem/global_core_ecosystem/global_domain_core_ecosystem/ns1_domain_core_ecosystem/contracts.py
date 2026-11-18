"""Provider identity contract for IBM NS1 Connect."""

PROVIDER_ID = "ns1"
PROVIDER_NAME = "IBM NS1 Connect"
PROVIDER_SCOPE = "DNS traffic steering API"
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
