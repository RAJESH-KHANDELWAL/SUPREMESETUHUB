"""Read-only service facade for Bada Business service-work capabilities."""
from .catalog import get_catalog, list_business_capabilities, list_work_models
from .orchestrator import dependency_map, health


class GlobalIndependentWorkServiceBusinessCoreService:
    def status(self) -> dict:
        return get_catalog()

    def list_work_models(self) -> dict:
        items = list_work_models()
        return {"success": True, "count": len(items), "work_models": items}

    def list_business_capabilities(self) -> dict:
        items = list_business_capabilities()
        return {"success": True, "count": len(items), "business_capabilities": items}

    def health(self) -> dict:
        return health()

    def dependency_map(self) -> dict:
        return dependency_map()
