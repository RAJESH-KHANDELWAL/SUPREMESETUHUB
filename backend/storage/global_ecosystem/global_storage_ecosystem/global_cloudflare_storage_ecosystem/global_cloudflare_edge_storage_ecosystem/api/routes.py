"""Read-only local health boundary."""
from ..ecosystem_service import StorageCategoryService
def get_health() -> dict:
    return StorageCategoryService().describe()
