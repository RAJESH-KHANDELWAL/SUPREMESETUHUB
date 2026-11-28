"""Read-only service facade."""
from .catalog import get_catalog, list_work_models
from .orchestrator import health, dependency_map

class GlobalIndependentWorkCoreService:
    def status(self) -> dict:
        return get_catalog()

    def list_work_models(self) -> dict:
        items = list_work_models()
        return {"success": True, "count": len(items), "work_models": items}

    def health(self) -> dict:
        return health()

    def dependency_map(self) -> dict:
        return dependency_map()
