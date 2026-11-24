"""B2C ECOMMERCE MARKETPLACES channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "b2c_ecommerce_marketplaces"
def get_record():
    return get_channel(CHANNEL_ID)
