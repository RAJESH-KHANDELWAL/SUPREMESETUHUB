"""Provider identity contract for IANA Root Zone Database."""

PROVIDER_ID = "iana"
PROVIDER_NAME = "IANA Root Zone Database"
PROVIDER_SCOPE = "Root zone and TLD registry information"
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
