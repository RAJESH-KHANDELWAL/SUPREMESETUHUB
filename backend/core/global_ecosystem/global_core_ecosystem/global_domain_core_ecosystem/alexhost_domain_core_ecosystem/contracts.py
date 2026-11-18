"""Provider identity contract for AlexHost."""

PROVIDER_ID = "alexhost"
PROVIDER_NAME = "AlexHost"
PROVIDER_SCOPE = "Hosting and domain-related services reference; API/registrar support requires verification"
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
