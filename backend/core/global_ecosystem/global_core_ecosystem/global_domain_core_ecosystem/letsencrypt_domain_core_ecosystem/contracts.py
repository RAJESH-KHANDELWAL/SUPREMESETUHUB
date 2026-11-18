"""Provider identity contract for Let's Encrypt."""

PROVIDER_ID = "letsencrypt"
PROVIDER_NAME = "Let's Encrypt"
PROVIDER_SCOPE = "Automated TLS certificate issuance for domains"
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
