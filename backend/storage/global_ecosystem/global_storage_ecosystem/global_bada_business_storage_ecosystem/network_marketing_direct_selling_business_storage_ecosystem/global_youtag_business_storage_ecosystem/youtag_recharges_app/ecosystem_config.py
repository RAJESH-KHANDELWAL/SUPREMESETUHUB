"""Runtime configuration for YOUTAG_RECHARGES_APP; no secrets in source."""
import os
APP_ID="YOUTAG_RECHARGES_APP"
def get_config()->dict:return {"enabled":os.getenv("YOUTAG_RECHARGES_APP_ENABLED","true").lower()=="true","connection_state":"NOT_CONFIGURED","credentials_configured":False}
