"""Framework-neutral routes for the GOOGLE_STORAGE_ECOSYSTEM catalog."""
from ..ecosystem_service import EcosystemService


def get_catalog_status() -> dict:
    return EcosystemService().describe()


def get_catalog_health() -> dict:
    return EcosystemService().health()
