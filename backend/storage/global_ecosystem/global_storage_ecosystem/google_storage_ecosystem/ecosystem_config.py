"""Configuration for the GOOGLE_STORAGE_ECOSYSTEM catalog root."""
import os

ECOSYSTEM_ID = "GOOGLE_STORAGE_ECOSYSTEM"
ENV_PREFIX = ECOSYSTEM_ID


def get_config() -> dict:
    return {
        "enabled": os.getenv(f"{ENV_PREFIX}_ENABLED", "true").lower() == "true",
        "environment": os.getenv("APP_ENV", "development"),
        "connection_state": "NOT_CONFIGURED",
        "provider_credentials_configured": False,
        "catalog_only": True,
    }
