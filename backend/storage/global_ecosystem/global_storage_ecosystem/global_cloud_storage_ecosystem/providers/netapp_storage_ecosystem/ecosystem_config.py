"""Provider runtime configuration; credentials are not stored here."""
import os
PROVIDER_ID = "NETAPP"

def get_config() -> dict:
    return {"enabled": os.getenv("NETAPP_STORAGE_ENABLED", "false").lower() == "true", "credentials_configured": False, "secret_source": "external_secret_manager"}
