"""Read-only public service for Global Storage Core Ecosystem."""
from __future__ import annotations
from typing import Any
from .catalog import get_storage_core_catalog
from .orchestrator import GlobalStorageCoreOrchestrator

class GlobalStorageCoreEcosystemService:
    NAME = "GLOBAL STORAGE CORE ECOSYSTEM"
    def __init__(self) -> None:
        self.orchestrator = GlobalStorageCoreOrchestrator()
    def status(self) -> dict[str, Any]:
        catalog = get_storage_core_catalog(); health = self.orchestrator.health()
        return {"success":True,"ecosystem_id":catalog["ecosystem_id"],"name":self.NAME,"status":catalog["status"],"provider_count":health["provider_count"],"enabled_provider_count":health["enabled_provider_count"],"live_connection_verified":False,"storage_operations_performed":0,"health":health}
    def list_providers(self) -> dict[str, Any]: return self.orchestrator.list_providers()
    def get_provider(self, provider_id: str) -> dict[str, Any] | None: return self.orchestrator.get_provider(provider_id)
    def health(self) -> dict[str, Any]: return self.orchestrator.health()
    def dependency_map(self) -> dict[str, Any]: return self.orchestrator.dependency_map()
