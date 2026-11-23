"""Application-facing read-only service for transport and mobility Core."""
from .orchestrator import TransportMobilityCoreOrchestrator
class TransportMobilityCoreService:
    def __init__(self): self.orchestrator = TransportMobilityCoreOrchestrator()
    def status(self): return self.orchestrator.status()
    def discover(self, query=None): return self.orchestrator.discover(query)
