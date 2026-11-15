"""Top-level Adobe ecosystem descriptor."""
from .what_adobe_provides.catalog import ADOBE_PRODUCT_FAMILIES

ADOBE_ECOSYSTEM = {
    "provider_id": "adobe",
    "name": "Adobe",
    "catalog_status": "INITIALIZED",
    "product_family_count": len(ADOBE_PRODUCT_FAMILIES),
    "storage_path": "what_adobe_provides/storage_ecosystem",
    "live_provider_connection_verified": False,
}

def describe_adobe_ecosystem():
    return dict(ADOBE_ECOSYSTEM)

__all__ = ["ADOBE_ECOSYSTEM", "describe_adobe_ecosystem"]
