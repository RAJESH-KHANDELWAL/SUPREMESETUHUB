"""Runtime configuration; secrets must come from an approved secret manager."""
import os
def get_config() -> dict:
 return {"enabled":os.getenv("GLOBAL_DOMAIN_STORAGE_ECOSYSTEM_ENABLED","true").lower()=="true","environment":os.getenv("APP_ENV","development"),"credentials_configured":False,"secret_source":"runtime_environment_or_secret_manager","external_connection_state":"NOT_CONFIGURED"}
