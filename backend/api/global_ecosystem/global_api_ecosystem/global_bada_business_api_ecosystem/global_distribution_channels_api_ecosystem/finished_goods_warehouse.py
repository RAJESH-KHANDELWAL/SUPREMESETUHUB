"""FINISHED GOODS WAREHOUSE channel module; canonical record lives in catalog.py."""
from .catalog import get_channel
CHANNEL_ID = "finished_goods_warehouse"
def get_record():
    return get_channel(CHANNEL_ID)
