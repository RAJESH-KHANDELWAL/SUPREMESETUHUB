"""Runtime configuration for YOUTAG_WELLNESS_APP; no secrets in source."""
import os
APP_ID="YOUTAG_WELLNESS_APP"
def get_config()->dict:return {"enabled":os.getenv("YOUTAG_WELLNESS_APP_ENABLED","true").lower()=="true","connection_state":"NOT_CONFIGURED","credentials_configured":False}
