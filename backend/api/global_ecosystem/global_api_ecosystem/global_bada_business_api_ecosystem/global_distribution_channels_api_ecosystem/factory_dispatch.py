"""FACTORY DISPATCH channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "factory_dispatch"
def get_record():
    return get_channel(CHANNEL_ID)
