"""Framework-neutral read-only catalog handlers; no external provider I/O."""
from ..catalog_api import GlobalIntegrationsStorageCatalog

_catalog = GlobalIntegrationsStorageCatalog()

def ecosystem_status() -> dict:
    return _catalog.health()

def list_integrations(category: str | None = None) -> list[dict[str, str]]:
    return _catalog.list(category)

def get_integration(name_or_category: str) -> dict[str, str] | None:
    return _catalog.get(name_or_category)
