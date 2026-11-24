"""Final customer handover channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "end_customer_handover"
def get_record():
    return get_channel(CHANNEL_ID)
