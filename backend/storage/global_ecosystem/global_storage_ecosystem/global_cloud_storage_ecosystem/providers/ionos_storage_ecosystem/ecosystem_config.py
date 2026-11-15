"""Provider runtime configuration; credentials are not stored here."""
import os
PROVIDER_ID = "IONOS"

def get_config() -> dict:
    return {"enabled": os.getenv("IONOS_STORAGE_ENABLED", "false").lower() == "true", "credentials_configured": False, "secret_source": "external_secret_manager"}
