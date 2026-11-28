"""Runtime configuration; credentials are never stored in this package."""
import os

def get_config() -> dict:
    return {
        "enabled": os.getenv("GLOBAL_CLOUDFLARE_STORAGE_ECOSYSTEM_ENABLED", "true").lower() == "true",
        "provider_id": "CLOUDFLARE",
        "connection_state": "NOT_CONFIGURED",
        "storage_operations_enabled": False,
    }
