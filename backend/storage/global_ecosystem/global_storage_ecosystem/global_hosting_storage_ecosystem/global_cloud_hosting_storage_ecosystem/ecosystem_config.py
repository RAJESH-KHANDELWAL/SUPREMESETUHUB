"""Runtime config for GLOBAL_CLOUD_HOSTING_HOSTING_STORAGE_ECOSYSTEM; never store secrets here."""
import os
ECOSYSTEM_ID="GLOBAL_CLOUD_HOSTING_HOSTING_STORAGE_ECOSYSTEM"
def get_config() -> dict:
 return {"enabled":os.getenv(ECOSYSTEM_ID+"_ENABLED","true").lower()=="true","environment":os.getenv("APP_ENV","development"),"connection_state":"NOT_CONFIGURED","credentials_configured":False}
