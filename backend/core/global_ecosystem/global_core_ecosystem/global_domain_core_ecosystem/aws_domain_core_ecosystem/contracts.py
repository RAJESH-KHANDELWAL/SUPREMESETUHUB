"""Provider identity contract for Amazon Route 53."""

PROVIDER_ID = "aws"
PROVIDER_NAME = "Amazon Route 53"
PROVIDER_SCOPE = "DNS hosting and domain registration transfer support"
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
