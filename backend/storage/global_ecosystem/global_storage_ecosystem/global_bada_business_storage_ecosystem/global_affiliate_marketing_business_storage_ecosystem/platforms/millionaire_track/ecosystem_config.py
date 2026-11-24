"""Runtime config for MILLIONAIRE_TRACK; no embedded platform credentials."""
import os
PLATFORM_ID="MILLIONAIRE_TRACK"
def get_config()->dict:return {"enabled":os.getenv("MILLIONAIRE_TRACK_ENABLED","true").lower()=="true","connection_state":"NOT_CONFIGURED","credentials_configured":False}
