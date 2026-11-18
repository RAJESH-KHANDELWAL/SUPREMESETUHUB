"""Provider identity contract for FlokiNET."""

PROVIDER_ID = "flokinet"
PROVIDER_NAME = "FlokiNET"
PROVIDER_SCOPE = "Hosting provider reference; registrar and API capabilities require verification"
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
