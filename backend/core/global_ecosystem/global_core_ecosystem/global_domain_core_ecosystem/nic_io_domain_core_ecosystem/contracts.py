"""Provider identity contract for NIC.IO."""

PROVIDER_ID = "nic_io"
PROVIDER_NAME = "NIC.IO"
PROVIDER_SCOPE = "Registry for .io domains"
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
