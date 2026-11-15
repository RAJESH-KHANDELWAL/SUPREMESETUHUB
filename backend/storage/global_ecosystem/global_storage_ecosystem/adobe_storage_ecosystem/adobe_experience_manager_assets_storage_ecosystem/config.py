"""Environment-only settings; secrets remain in the central Adobe integration layer."""
import os
ENV_PREFIX="ADOBE_EXPERIENCE_MANAGER_ASSETS"
def get_config()->dict:
    return {"enabled":os.getenv(f"{ENV_PREFIX}_ENABLED","true").strip().lower()=="true","environment":os.getenv("APP_ENV","development"),"connection_state":"NOT_CONFIGURED","credentials_configured":False,"secret_source":"central_secret_manager_via_adobe_api_integration"}
