"""COMPANY DEPOT channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "company_depot"
def get_record():
    return get_channel(CHANNEL_ID)
