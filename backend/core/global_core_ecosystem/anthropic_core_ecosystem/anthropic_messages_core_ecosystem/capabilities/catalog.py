"""Registered Core capabilities; metadata only."""
from ..ecosystem_config import PRODUCT_ID, API_NAME, AVAILABILITY
CAPABILITIES={
 "product_id":PRODUCT_ID,"api_surface":API_NAME,"availability":AVAILABILITY,
 "capabilities":["ANTHROPIC_MESSAGES_CREATE","ANTHROPIC_MESSAGES_STREAM","ANTHROPIC_MESSAGES_TOOL_USE"],"sensitive":False,
 "write_enabled":False,"live":False
}
