"""Credential-free configuration for the GLOBAL CLOUD STORAGE catalog."""
import os

PACKAGE_ID = "global_cloud_storage_ecosystem"
ECOSYSTEM_ID = "GLOBAL_CLOUD_STORAGE_ECOSYSTEM"


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def get_config() -> dict:
    """Return local foundation configuration; never load provider secrets here."""
    return {
        "package_id": PACKAGE_ID,
        "ecosystem_id": ECOSYSTEM_ID,
        "enabled": _env_bool("GLOBAL_CLOUD_STORAGE_ECOSYSTEM_ENABLED", True),
        "environment": os.getenv("APP_ENV", "development"),
        "credentials_configured": False,
        "connection_state": "NOT_CONFIGURED",
        "external_connections_verified": False,
        "storage_operations_enabled": False,
        "secret_source": "external_secret_manager",
    }
