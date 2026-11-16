"""CARRYING FORWARDING AGENTS channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "carrying_forwarding_agents"
def get_record():
    return get_channel(CHANNEL_ID)
