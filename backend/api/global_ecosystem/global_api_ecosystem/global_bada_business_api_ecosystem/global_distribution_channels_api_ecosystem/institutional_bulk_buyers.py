"""INSTITUTIONAL BULK BUYERS channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "institutional_bulk_buyers"
def get_record():
    return get_channel(CHANNEL_ID)
