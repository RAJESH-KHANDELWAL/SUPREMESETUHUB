"""Registered Core capabilities; metadata only."""
from ..ecosystem_config import PRODUCT_ID, API_NAME, AVAILABILITY
CAPABILITIES={
 "product_id":PRODUCT_ID,"api_surface":API_NAME,"availability":AVAILABILITY,
 "capabilities":["ANTHROPIC_CREDENTIAL_READINESS","ANTHROPIC_WORKLOAD_IDENTITY_BOUNDARY","ANTHROPIC_CREDENTIAL_ROTATION_BOUNDARY"],"sensitive":True,
 "write_enabled":False,"live":False
}
