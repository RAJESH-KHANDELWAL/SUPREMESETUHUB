"""Registered Core capabilities; metadata only."""
from ..ecosystem_config import PRODUCT_ID, API_NAME, AVAILABILITY
CAPABILITIES={
 "product_id":PRODUCT_ID,"api_surface":API_NAME,"availability":AVAILABILITY,
 "capabilities":["ANTHROPIC_FILES_LIST","ANTHROPIC_FILES_UPLOAD","ANTHROPIC_FILES_RETRIEVE","ANTHROPIC_FILES_DELETE"],"sensitive":True,
 "write_enabled":False,"live":False
}
