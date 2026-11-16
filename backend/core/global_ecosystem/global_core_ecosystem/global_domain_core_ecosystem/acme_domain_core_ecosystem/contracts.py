"""Provider identity contract for ACME protocol."""

PROVIDER_ID = "acme"
PROVIDER_NAME = "ACME protocol"
PROVIDER_SCOPE = "Automated certificate management protocol"
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
