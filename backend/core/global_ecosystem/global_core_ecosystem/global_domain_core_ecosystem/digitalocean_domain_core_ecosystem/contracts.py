"""Provider identity contract for DigitalOcean."""

PROVIDER_ID = "digitalocean"
PROVIDER_NAME = "DigitalOcean"
PROVIDER_SCOPE = "DNS records and domain zones"
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
