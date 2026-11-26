"""Public read-only service facade."""
from __future__ import annotations
from .catalog import get_catalog
from .orchestrator import CoreOrchestrator
class VideoCoreService:
    def __init__(self): self.orchestrator = CoreOrchestrator()
    def status(self) -> dict:
        result = self.orchestrator.status()
        return {"success": True, "name": get_catalog()["name"], **result}
    def list_providers(self, enabled_only: bool = False) -> dict: return self.orchestrator.list_providers(enabled_only)
    def get_provider(self, provider_id: str): return self.orchestrator.get_provider(provider_id)
    def list_domains(self) -> dict: return self.orchestrator.domains()
    def dependency_map(self) -> dict: return self.orchestrator.dependency_map()
