"""Runtime configuration without embedded credentials."""
import os

def get_config() -> dict:
    return {
        "enabled": os.getenv("GLOBAL_CLOUDFLARE_DURABLE_OBJECTS_STORAGE_ECOSYSTEM_ENABLED", "true").lower() == "true",
        "provider_id": "CLOUDFLARE",
        "connection_state": "NOT_CONFIGURED",
        "storage_operations_enabled": False,
    }
