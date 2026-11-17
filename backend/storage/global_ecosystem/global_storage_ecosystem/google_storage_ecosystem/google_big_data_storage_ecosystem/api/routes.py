"""Framework-neutral API handlers for GOOGLE_BIG_DATA_STORAGE_ECOSYSTEM."""
from ..ecosystem_service import CategoryEcosystemService
def get_ecosystem_status() -> dict:
    return CategoryEcosystemService().describe()
def get_health() -> dict:
    return CategoryEcosystemService().health()
