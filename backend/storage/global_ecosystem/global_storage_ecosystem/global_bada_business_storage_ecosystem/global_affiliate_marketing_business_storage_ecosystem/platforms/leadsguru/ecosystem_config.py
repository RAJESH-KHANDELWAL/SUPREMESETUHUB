"""Runtime config for LEADSGURU; no embedded platform credentials."""
import os
PLATFORM_ID="LEADSGURU"
def get_config()->dict:return {"enabled":os.getenv("LEADSGURU_ENABLED","true").lower()=="true","connection_state":"NOT_CONFIGURED","credentials_configured":False}
