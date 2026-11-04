"""MODERN RETAIL CHAINS channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "modern_retail_chains"
def get_record():
    return get_channel(CHANNEL_ID)
