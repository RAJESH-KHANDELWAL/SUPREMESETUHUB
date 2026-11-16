"""Read-only provider discovery and health orchestration."""
from .catalog import list_providers, validate_catalog
def list_provider_packages():
    return list_providers()
def health():
    result = validate_catalog()
    return {"status": "healthy" if result["valid"] and not result["missing_packages"] else "degraded", **result}
