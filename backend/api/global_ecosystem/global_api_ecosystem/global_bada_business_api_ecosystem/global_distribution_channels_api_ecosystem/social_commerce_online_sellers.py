"""SOCIAL COMMERCE ONLINE SELLERS channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "social_commerce_online_sellers"
def get_record():
    return get_channel(CHANNEL_ID)
