"""Public read-only service facade for Global Database Core."""
from .manager import (
    ECOSYSTEM_ID,
    get_provider,
    list_categories,
    list_providers,
    validate_catalog,
)
from .policy import get_policy


def get_status():
    validation = validate_catalog()
    return {
        "success": validation["valid"],
        "ecosystem_id": ECOSYSTEM_ID,
        "status": "catalog_available" if validation["valid"] else "catalog_invalid",
        "implementation_status": "CATALOG_ONLY",
        "live_connection_verified": False,
        "provider_count": validation["provider_count"],
        "category_count": validation["category_count"],
    }


def list_provider_records():
    providers = list_providers()
    return {"success": True, "count": len(providers), "providers": providers}


def get_provider_record(provider_id: str):
    return get_provider(provider_id)


def get_capability_categories():
    return list_categories()


def get_security_policy():
    return get_policy()
