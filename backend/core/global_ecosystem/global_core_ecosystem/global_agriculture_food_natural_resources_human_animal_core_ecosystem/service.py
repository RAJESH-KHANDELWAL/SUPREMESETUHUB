"""Public read-only service facade."""
from __future__ import annotations
from .catalog import get_catalog
from .orchestrator import AgricultureCoreOrchestrator

class AgricultureCoreService:
    def __init__(self):
        self.orchestrator = AgricultureCoreOrchestrator()

    def status(self):
        catalog = get_catalog()
        return {"success": True, "ecosystem": catalog, "health": self.orchestrator.health(), "dependency_map": self.orchestrator.dependency_map()}
