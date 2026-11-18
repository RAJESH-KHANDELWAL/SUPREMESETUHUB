"""Read-only diagnostic tools for the SERVER ecosystem."""
from ..catalog import list_providers, list_service_types

def server_diagnostics(service):
    """Return local SERVER diagnostics without opening external connections."""
    result = service.health()
    return {
        "domain": result["domain"],
        "ecosystem": result["ecosystem"],
        "status": result["status"],
        "server_registry": result["server_registry"],
        "configured_provider_count": result["configured_provider_count"],
        "external_connections": result["external_connections"],
        "runtime": result["runtime"],
    }

def server_catalog():
    return {"providers": list_providers(), "service_types": list_service_types()}

__all__ = ["server_diagnostics", "server_catalog"]
