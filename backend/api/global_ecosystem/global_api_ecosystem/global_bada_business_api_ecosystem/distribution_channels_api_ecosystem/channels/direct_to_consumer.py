"""Direct-to-consumer channel module; canonical definition lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "direct_to_consumer"
def get_record():
    return get_channel(CHANNEL_ID)
