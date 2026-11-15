"""IMPORT EXPORT CHANNEL PARTNERS channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "import_export_channel_partners"
def get_record():
    return get_channel(CHANNEL_ID)
