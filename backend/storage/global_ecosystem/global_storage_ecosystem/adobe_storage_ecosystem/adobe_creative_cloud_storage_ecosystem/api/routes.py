"""Framework-neutral handlers for ADOBE_CREATIVE_CLOUD_STORAGE_ECOSYSTEM."""
from ..ecosystem_service import CategoryEcosystemService

def get_ecosystem_status() -> dict:
    return CategoryEcosystemService().describe()

def get_health() -> dict:
    return CategoryEcosystemService().health()
