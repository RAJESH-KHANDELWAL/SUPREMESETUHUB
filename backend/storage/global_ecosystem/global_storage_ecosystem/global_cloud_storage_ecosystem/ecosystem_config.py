"""Runtime configuration without embedded credentials."""
import os

PACKAGE_ID = "global_cloud_storage_ecosystem"


def get_config() -> dict:
    return {
        "enabled": os.getenv("GLOBAL_CLOUD_STORAGE_ECOSYSTEM_ENABLED", "true").lower() == "true",
        "environment": os.getenv("APP_ENV", "development"),
        "credentials_configured": False,
        "secret_source": "external_secret_manager",
    }
