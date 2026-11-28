"""Status-only service contract; no AWS API calls are made here."""
from .ecosystem_config import get_config

def get_status() -> dict:
    config = get_config()
    return {
        "provider": "AWS",
        "category": "SNOW_FAMILY",
        "display_name": "AWS Snow Family",
        "connection_state": "NOT_CONFIGURED",
        "configured": False,
        "storage_operations_enabled": False,
        "enabled_flag_requested": config["enabled"],
    }
