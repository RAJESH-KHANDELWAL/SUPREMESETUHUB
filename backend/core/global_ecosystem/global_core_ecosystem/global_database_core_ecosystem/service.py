"""Public read-only service facade for Global Database Core."""
from .catalog import ECOSYSTEM_ID, list_providers, get_provider, list_categories, validate_catalog
from .policy import get_policy

def get_status():
    validation = validate_catalog()
    return {"success": validation["valid"], "ecosystem_id": ECOSYSTEM_ID, "status": "catalog_available" if validation["valid"] else "catalog_invalid", "implementation_status": "CATALOG_ONLY", "live_connection_verified": False, "provider_count": validation["provider_count"], "category_count": validation["category_count"]}

def list_provider_records():
    return {"success": True, "count": len(list_providers()), "providers": list_providers()}

def get_provider_record(provider_id: str):
    return get_provider(provider_id)

def get_capability_categories():
    return list_categories()

def get_security_policy():
    return get_policy()
