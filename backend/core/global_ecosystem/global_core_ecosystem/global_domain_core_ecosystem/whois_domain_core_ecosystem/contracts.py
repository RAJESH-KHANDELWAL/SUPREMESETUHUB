"""Provider identity contract for WHOIS."""

PROVIDER_ID = "whois"
PROVIDER_NAME = "WHOIS"
PROVIDER_SCOPE = "Domain registration lookup protocol/reference"
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
