"""DIRECT TO CONSUMER channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "direct_to_consumer"
def get_record():
    return get_channel(CHANNEL_ID)
