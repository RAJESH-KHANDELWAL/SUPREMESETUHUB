"""Registered Core capabilities; metadata only."""
from ..ecosystem_config import PRODUCT_ID, API_NAME, AVAILABILITY
CAPABILITIES={
 "product_id":PRODUCT_ID,"api_surface":API_NAME,"availability":AVAILABILITY,
 "capabilities":["ANTHROPIC_MODELS_LIST","ANTHROPIC_MODEL_METADATA"],"sensitive":False,
 "write_enabled":False,"live":False
}
