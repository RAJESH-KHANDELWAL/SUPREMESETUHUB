"""Framework-neutral API handlers for GLOBAL_DEDICATED_SERVER_HOSTING_HOSTING_STORAGE_ECOSYSTEM."""
from ..ecosystem_service import CategoryEcosystemService
def get_ecosystem_status()->dict: return CategoryEcosystemService().describe()
def get_health()->dict: return CategoryEcosystemService().health()
