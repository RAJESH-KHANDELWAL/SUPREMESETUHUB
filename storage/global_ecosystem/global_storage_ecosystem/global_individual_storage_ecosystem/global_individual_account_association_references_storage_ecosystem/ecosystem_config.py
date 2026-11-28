"""Safe-by-default runtime configuration; never store credentials or secrets here."""
import os

ECOSYSTEM_ID = "GLOBAL_INDIVIDUAL_ACCOUNT_ASSOCIATION_REFERENCES_STORAGE_ECOSYSTEM"
ENV_PREFIX = "GLOBAL_INDIVIDUAL_ACCOUNT_ASSOCIATION_REFERENCES_STORAGE_ECOSYSTEM"

def get_config() -> dict:
    return {
        "enabled": os.getenv(f"{ENV_PREFIX}_ENABLED", "false").lower() == "true",
        "environment": os.getenv("APP_ENV", "development"),
        "connection_state": "NOT_CONFIGURED",
        "credentials_configured": False,
        "storage_operations_enabled": False,
    }
