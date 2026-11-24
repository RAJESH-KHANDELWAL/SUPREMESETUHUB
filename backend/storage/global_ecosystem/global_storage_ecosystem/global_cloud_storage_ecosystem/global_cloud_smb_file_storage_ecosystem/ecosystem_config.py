"""Runtime configuration for GLOBAL_CLOUD_SMB_FILE_STORAGE_ECOSYSTEM; secrets must remain external."""
import os

ECOSYSTEM_ID = "GLOBAL_CLOUD_SMB_FILE_STORAGE_ECOSYSTEM"
ENV_PREFIX = "GLOBAL_CLOUD_SMB_FILE_STORAGE_ECOSYSTEM"

def get_config() -> dict:
    return {
        "enabled": os.getenv(f"{ENV_PREFIX}_ENABLED", "true").lower() == "true",
        "environment": os.getenv("APP_ENV", "development"),
        "connection_state": "NOT_CONFIGURED",
        "credentials_configured": False,
    }
