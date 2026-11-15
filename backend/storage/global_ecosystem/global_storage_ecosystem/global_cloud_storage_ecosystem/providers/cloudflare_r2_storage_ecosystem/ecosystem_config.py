"""Provider runtime configuration; credentials are not stored here."""
import os
PROVIDER_ID = "CLOUDFLARE_R2"

def get_config() -> dict:
    return {"enabled": os.getenv("CLOUDFLARE_R2_STORAGE_ENABLED", "false").lower() == "true", "credentials_configured": False, "secret_source": "external_secret_manager"}
