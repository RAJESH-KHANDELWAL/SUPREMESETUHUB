"""Secret-free runtime configuration."""
import os

def get_config() -> dict:
    return {"enabled": os.getenv("GLOBAL_DEVELOPER_STORAGE_ENABLED", "false").lower() == "true", "credentials_configured": False, "secret_source": "approved_secret_manager"}
