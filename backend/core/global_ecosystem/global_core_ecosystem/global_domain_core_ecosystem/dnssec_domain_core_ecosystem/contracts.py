"""Provider identity contract for DNSSEC."""

PROVIDER_ID = "dnssec"
PROVIDER_NAME = "DNSSEC"
PROVIDER_SCOPE = "DNS security extension ecosystem"
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
