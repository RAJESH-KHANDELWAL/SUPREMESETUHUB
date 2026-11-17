"""Metadata-only capability declaration for IBM LANGUAGE."""
from ..ecosystem_config import ECOSYSTEM_ID, PROVIDER_ID

CAPABILITIES = {
    "provider_id": PROVIDER_ID,
    "ecosystem_id": ECOSYSTEM_ID,
    "registered_capabilities": [
        "HUMAN_LANGUAGE_PROVIDER_METADATA",
        "CAPABILITY_DISCOVERY_METADATA",
        "CONNECTION_READINESS_METADATA",
    ],
    "api_operations_enabled": False,
    "live": False,
}
