"""Provider runtime configuration; credentials are not stored here."""
import os
PROVIDER_ID = "PURE_STORAGE"

def get_config() -> dict:
    return {"enabled": os.getenv("PURE_STORAGE_STORAGE_ENABLED", "false").lower() == "true", "credentials_configured": False, "secret_source": "external_secret_manager"}
