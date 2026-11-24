"""Canonical manager for Global Software Core Ecosystem."""
from __future__ import annotations
from typing import Any
from .orchestrator import GlobalSoftwareCoreOrchestrator
from .domain_runtime import SoftwareCoreDomainManager
from .service import GlobalSoftwareCoreService
class GlobalSoftwareCoreManager:
    NAME="GLOBAL SOFTWARE CORE ECOSYSTEM"
    ECOSYSTEM_ID="GLOBAL-SOFTWARE-CORE-ECOSYSTEM"
    def __init__(self): self._orchestrator=GlobalSoftwareCoreOrchestrator(); self._service=GlobalSoftwareCoreService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def health(self) -> dict[str, Any]: return self._orchestrator.health()
    def list_providers(self, *, enabled_only: bool=False): return self._orchestrator.list_providers(enabled_only=enabled_only)
    def get_provider(self, provider_id: str): return self._orchestrator.get_provider(provider_id)
    def list_domains(self): return self._orchestrator.domains()
    def list_domain_inventory(self): return self._orchestrator.domain_inventory()
    def get_domain_manager(self, domain_id: str): return SoftwareCoreDomainManager(domain_id)
def get_manager() -> GlobalSoftwareCoreManager: return GlobalSoftwareCoreManager()
__all__=["GlobalSoftwareCoreManager","get_manager"]
