"""Channel module for factory dispatch.

The canonical channel record is maintained in catalog.py to prevent duplicate
business definitions across the ecosystem.
"""

from .catalog import get_channel

CHANNEL_ID = "factory_dispatch"

def get_record():
    """Return the canonical channel definition."""
    return get_channel(CHANNEL_ID)
