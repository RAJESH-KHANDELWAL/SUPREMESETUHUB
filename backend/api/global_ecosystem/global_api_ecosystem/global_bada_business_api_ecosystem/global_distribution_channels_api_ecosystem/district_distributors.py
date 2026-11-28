"""DISTRICT DISTRIBUTORS channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "district_distributors"
def get_record():
    return get_channel(CHANNEL_ID)
