"""Canonical Cohere capability-to-package inventory.

Derived from the provider catalog to prevent duplicate registry definitions.
"""
from .catalog import CAPABILITIES

PRODUCT_CATALOG = {
    capability: {
        "package": metadata["package"],
        "status": metadata["status"],
        "mode": metadata["mode"],
        "live_enabled": metadata["live_enabled"],
    }
    for capability, metadata in CAPABILITIES.items()
}


def list_cohere_products():
    return {name: dict(metadata) for name, metadata in PRODUCT_CATALOG.items()}
