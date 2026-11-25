"""Reusable read-only service for one cultural domain Core package."""
from .domain_runtime import CulturalCoreDomainManager
class CulturalCoreModuleService:
    def __init__(self,domain_id: str): self.domain=CulturalCoreDomainManager(domain_id)
    def status(self): return self.domain.status()
    def list_offerings(self): return self.domain.list_offerings()
    def search(self,query: str): return self.domain.search(query)
