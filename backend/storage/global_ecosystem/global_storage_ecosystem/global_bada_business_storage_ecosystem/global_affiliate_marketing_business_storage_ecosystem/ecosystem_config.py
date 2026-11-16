"""Runtime configuration without embedded secrets."""
import os
ECOSYSTEM_ID="GLOBAL_AFFILIATE_MARKETING_BUSINESS_STORAGE_ECOSYSTEM"
def get_config()->dict:return {"enabled":os.getenv("GLOBAL_AFFILIATE_MARKETING_BUSINESS_STORAGE_ECOSYSTEM_ENABLED","true").lower()=="true","connection_state":"NOT_CONFIGURED","credentials_configured":False,"environment":os.getenv("APP_ENV","development")}
