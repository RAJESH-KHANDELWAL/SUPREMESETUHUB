"""B2B MARKETPLACES channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "b2b_marketplaces"
def get_record():
    return get_channel(CHANNEL_ID)
