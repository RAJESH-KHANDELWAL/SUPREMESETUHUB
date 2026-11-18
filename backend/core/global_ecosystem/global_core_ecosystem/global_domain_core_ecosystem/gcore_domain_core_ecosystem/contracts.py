"""Provider identity contract for Gcore."""

PROVIDER_ID = "gcore"
PROVIDER_NAME = "Gcore"
PROVIDER_SCOPE = "DNS and edge network services"
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
