"""Provider identity contract for KEY-SYSTEMS."""

PROVIDER_ID = "keysystems"
PROVIDER_NAME = "KEY-SYSTEMS"
PROVIDER_SCOPE = "Registrar reseller API"
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
