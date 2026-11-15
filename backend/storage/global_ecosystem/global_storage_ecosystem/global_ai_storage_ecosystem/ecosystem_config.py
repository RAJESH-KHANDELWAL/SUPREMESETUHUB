"""Runtime configuration; secrets belong in an approved secret manager."""
import os
PACKAGE_ID = __package__.rsplit(".", 1)[-1]
ENV_PREFIX = PACKAGE_ID.upper()
def get_config() -> dict:
    return {"enabled":os.getenv(f"{ENV_PREFIX}_ENABLED","true").lower()=="true","environment":os.getenv("APP_ENV","development"),"connection_state":"NOT_CONFIGURED","credentials_configured":False,"secret_source":"runtime_environment_or_secret_manager"}
