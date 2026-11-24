"""Runtime configuration for ADOBE_LIGHTROOM_STORAGE_ECOSYSTEM; never store secrets in source."""
import os

ECOSYSTEM_ID = "ADOBE_LIGHTROOM_STORAGE_ECOSYSTEM"
ENV_PREFIX = ECOSYSTEM_ID

def get_config() -> dict:
    return {
        "enabled": os.getenv(f"{ENV_PREFIX}_ENABLED", "true").lower() == "true",
        "environment": os.getenv("APP_ENV", "development"),
        "connection_state": "NOT_CONFIGURED",
        "credentials_configured": False,
        "secret_source": "central_secret_manager_via_adobe_api_integration",
    }
