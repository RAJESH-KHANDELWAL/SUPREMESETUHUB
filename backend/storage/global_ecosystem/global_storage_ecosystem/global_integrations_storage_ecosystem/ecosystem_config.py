"""Safe-by-default runtime configuration for GLOBAL_INTEGRATIONS_STORAGE_ECOSYSTEM.

Credentials must be supplied through an approved runtime secret manager.
This package does not authenticate to providers or perform external I/O.
"""
import os

ECOSYSTEM_ID = "GLOBAL_INTEGRATIONS_STORAGE_ECOSYSTEM"
ENV_PREFIX = ECOSYSTEM_ID


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def get_config() -> dict:
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "enabled": _env_bool(f"{ENV_PREFIX}_ENABLED", False),
        "environment": os.getenv("APP_ENV", "development"),
        "credentials_configured": False,
        "secret_source": "approved_runtime_secret_manager",
        "external_connection_state": "NOT_CONFIGURED",
        "storage_operations_enabled": False,
    }
