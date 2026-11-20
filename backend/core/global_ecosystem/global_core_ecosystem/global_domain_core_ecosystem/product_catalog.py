"""Domain provider inventory; catalog-only references, not live integrations."""
from .catalog import PROVIDER_DIRECTORIES
DOMAIN_PROVIDER_CATALOG = tuple({"provider_id": p.removesuffix("_domain_core_ecosystem").upper(), "directory": p, "status": "CATALOG_ONLY", "connected": False} for p in PROVIDER_DIRECTORIES)
def list_provider_catalog():
    return [dict(item) for item in DOMAIN_PROVIDER_CATALOG]
