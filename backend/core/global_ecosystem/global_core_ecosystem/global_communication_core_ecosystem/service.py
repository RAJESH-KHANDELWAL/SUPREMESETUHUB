"""Read-only Communication Core orchestration service."""
from .catalog import ECOSYSTEM_ID, list_providers, list_categories, validate_catalog
def ecosystem_status():
    providers = list_providers()
    return {"ecosystem_id": ECOSYSTEM_ID, "provider_count": len(providers),
            "category_count": len(list_categories()), "connected_provider_count": 0,
            "live_messaging_enabled": False, "providers": providers,
            "catalog_validation": validate_catalog()}
def get_provider_status(provider_id):
    return next((p for p in list_providers() if p["provider_id"] == provider_id), None)
