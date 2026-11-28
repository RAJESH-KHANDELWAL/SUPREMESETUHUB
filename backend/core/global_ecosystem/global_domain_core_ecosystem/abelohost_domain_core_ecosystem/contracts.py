"""Provider identity contract for AbeloHost."""

PROVIDER_ID = "abelohost"
PROVIDER_NAME = "AbeloHost"
PROVIDER_SCOPE = "Privacy-focused hosting reference; domain registrar/API support requires verification"
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
