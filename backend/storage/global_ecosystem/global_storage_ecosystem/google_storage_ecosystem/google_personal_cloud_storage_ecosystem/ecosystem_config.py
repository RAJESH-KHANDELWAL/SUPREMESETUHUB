"""Configuration for GOOGLE_PERSONAL_CLOUD_STORAGE_ECOSYSTEM; no secrets are stored in source."""
import os

ECOSYSTEM_ID = "GOOGLE_PERSONAL_CLOUD_STORAGE_ECOSYSTEM"
ENV_PREFIX = ECOSYSTEM_ID


def get_config() -> dict:
    return {
        "enabled": os.getenv(f"{ENV_PREFIX}_ENABLED", "true").lower() == "true",
        "environment": os.getenv("APP_ENV", "development"),
        "connection_state": "NOT_CONFIGURED",
        "credentials_configured": False,
    }
