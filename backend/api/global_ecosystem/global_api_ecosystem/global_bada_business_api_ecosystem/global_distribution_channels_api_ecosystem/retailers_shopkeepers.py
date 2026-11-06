"""RETAILERS SHOPKEEPERS channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "retailers_shopkeepers"
def get_record():
    return get_channel(CHANNEL_ID)
