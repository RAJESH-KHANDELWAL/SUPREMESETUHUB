"""Provider runtime configuration; credentials are not stored here."""
import os
PROVIDER_ID = "HUAWEI_CLOUD"

def get_config() -> dict:
    return {"enabled": os.getenv("HUAWEI_CLOUD_STORAGE_ENABLED", "false").lower() == "true", "credentials_configured": False, "secret_source": "external_secret_manager"}
