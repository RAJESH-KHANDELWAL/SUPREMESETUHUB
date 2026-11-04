"""FRANCHISE STORES channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "franchise_stores"
def get_record():
    return get_channel(CHANNEL_ID)
