"""Channel module for b2c ecommerce marketplaces.

The canonical channel record is maintained in catalog.py to prevent duplicate
business definitions across the ecosystem.
"""

from .catalog import get_channel

CHANNEL_ID = "b2c_ecommerce_marketplaces"

def get_record():
    """Return the canonical channel definition."""
    return get_channel(CHANNEL_ID)
