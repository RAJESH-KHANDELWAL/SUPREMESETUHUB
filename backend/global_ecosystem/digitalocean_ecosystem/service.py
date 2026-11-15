"""Catalog and operation-planning facade for DigitalOcean.

No provider API request is made here. Runtime execution belongs in the
separately governed integration/runtime layers.
"""
from .catalog import list_capabilities, get_capability, search_capabilities
from .validation import validate_request
from .models import OperationRequest


def catalog():
    return list_capabilities()


def plan_operation(request):
    errors = validate_request(request)
    if errors:
        return {"ready": False, "errors": errors, "provider": "digitalocean"}
    capability = get_capability(request.capability_id)
    return {
        "ready": True,
        "provider": "digitalocean",
        "capability": capability,
        "action": request.action,
        "resource_type": request.resource_type or None,
        "region": request.region or None,
        "execution_performed": False,
        "execution_owner": "separate integration/runtime layers",
    }


def readiness():
    return {
        "provider": "digitalocean",
        "catalog_loaded": True,
        "capability_count": len(catalog()),
        "api_credentials_configured": False,
        "live_provider_connection_verified": False,
        "execution_enabled": False,
        "note": "Readiness is catalog-only; no credential or live API check is performed.",
    }
