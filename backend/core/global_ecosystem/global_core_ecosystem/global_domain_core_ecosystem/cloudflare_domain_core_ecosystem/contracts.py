"""Provider identity contract for Cloudflare."""

PROVIDER_ID = "cloudflare"
PROVIDER_NAME = "Cloudflare"
PROVIDER_SCOPE = "DNS zones, registrar domains, DNS records"
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
