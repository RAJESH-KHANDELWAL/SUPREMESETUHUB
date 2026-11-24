"""Domain provider inventory; catalog-only references, not live integrations."""
from .manager import PROVIDER_DIRECTORIES

DOMAIN_PROVIDER_CATALOG = tuple(
    {
        "provider_id": provider.removesuffix("_domain_core_ecosystem").upper(),
        "directory": provider,
        "status": "CATALOG_ONLY",
        "connected": False,
    }
    for provider in PROVIDER_DIRECTORIES
)


def list_provider_catalog():
    return [dict(item) for item in DOMAIN_PROVIDER_CATALOG]
