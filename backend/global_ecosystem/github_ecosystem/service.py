"""GitHub catalog and operation-planning facade; never executes provider calls."""
from .catalog import list_capabilities, get_capability, search_capabilities
from .validation import validate_request

def catalog(category=None):
    return list_capabilities(category=category)

def search(query):
    return search_capabilities(query)

def plan_operation(request):
    errors = validate_request(request)
    if errors:
        return {"ready": False, "errors": errors, "provider": "github"}
    return {
        "ready": True, "provider": "github",
        "capability": get_capability(request.capability_id),
        "action": request.action, "owner": request.owner or None,
        "repository": request.repository or None,
        "resource_type": request.resource_type or None,
        "execution_performed": False,
        "execution_owner": "separate integration/runtime layers",
    }

def readiness():
    return {
        "provider": "github", "catalog_loaded": True,
        "capability_count": len(catalog()), "credentials_loaded": False,
        "permissions_verified": False, "live_provider_connection_verified": False,
        "execution_enabled": False,
        "note": "Catalog-only readiness; no token is loaded and no GitHub API request is made.",
    }
