"""Canonical Python manager for GLOBAL VIDEO CORE ECOSYSTEM."""
from __future__ import annotations
from .service import VideoCoreService
from .domain_runtime import DomainManager
from .module_service import ProviderCoreService
class VideoCoreManager:
    NAME = "GLOBAL VIDEO CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-VIDEO-CORE-ECOSYSTEM"
    def __init__(self): self.service = VideoCoreService()
    def status(self) -> dict: return self.service.status()
    def health(self) -> dict: return self.service.status()
    def list_providers(self, enabled_only: bool = False) -> dict: return self.service.list_providers(enabled_only)
    def get_provider(self, provider_id: str): return self.service.get_provider(provider_id)
    def list_domains(self) -> dict: return self.service.list_domains()
    def get_domain_manager(self, domain_id: str) -> DomainManager: return DomainManager(domain_id)
    def get_provider_service(self, provider_id: str) -> ProviderCoreService: return ProviderCoreService(provider_id)
    def dependency_map(self) -> dict: return self.service.dependency_map()
def get_manager() -> VideoCoreManager: return VideoCoreManager()
__all__ = ["VideoCoreManager", "get_manager"]
