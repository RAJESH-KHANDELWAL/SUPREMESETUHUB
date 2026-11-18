"""Public read-only service facade for Global Developer Core."""
from __future__ import annotations
from .catalog import get_developer_core_catalog, list_developer_core_providers, get_developer_core_provider
from .orchestrator import GlobalDeveloperCoreOrchestrator

class GlobalDeveloperCoreService:
    ECOSYSTEM_ID = "GLOBAL-DEVELOPER-CORE-ECOSYSTEM"

    def __init__(self):
        self._orchestrator = GlobalDeveloperCoreOrchestrator()

    def status(self):
        return self._orchestrator.health()

    def catalog(self):
        return get_developer_core_catalog()

    def providers(self):
        return list_developer_core_providers()

    def provider(self, provider_id):
        return get_developer_core_provider(provider_id)

    def dependencies(self):
        return self._orchestrator.dependency_map()
