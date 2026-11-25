"""Application-facing read-only service for transport business Core."""
from .orchestrator import TransportBusinessCoreOrchestrator
class TransportBusinessCoreService:
    def __init__(self): self.orchestrator = TransportBusinessCoreOrchestrator()
    def status(self): return self.orchestrator.status()
    def discover(self, query=None): return self.orchestrator.discover(query)
