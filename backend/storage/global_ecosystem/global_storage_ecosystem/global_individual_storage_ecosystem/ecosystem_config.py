"""Runtime configuration for GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM.

Secrets and provider credentials must be supplied by a managed secret store,
never committed to this package.
"""
import os

ECOSYSTEM_ID = "GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM"
ENV_PREFIX = ECOSYSTEM_ID


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def get_config() -> dict:
    """Return safe-by-default local configuration."""
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "enabled": _env_bool(f"{ENV_PREFIX}_ENABLED", False),
        "environment": os.getenv("APP_ENV", "development"),
        "connection_state": "NOT_CONFIGURED",
        "credentials_configured": False,
        "storage_operations_enabled": False,
    }
