"""DISTRIBUTION CENTRES channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "distribution_centres"
def get_record():
    return get_channel(CHANNEL_ID)
