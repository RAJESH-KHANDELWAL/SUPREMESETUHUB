"""Provider identity contract for Porkbun."""

PROVIDER_ID = "porkbun"
PROVIDER_NAME = "Porkbun"
PROVIDER_SCOPE = "Domain registration and DNS"
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
