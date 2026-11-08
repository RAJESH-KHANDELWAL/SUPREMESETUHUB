"""Lowercase compatibility namespace for the server ENGINE ecosystem."""
from backend.engine.global_ecosystem.global_engine_ecosystem.global_server_engine_ecosystem import EcosystemService
class DomainService:
    domain = "SERVER"
    def __init__(self): self.ecosystem = EcosystemService()
    def describe(self): return self.ecosystem.describe()
__all__ = ["DomainService"]
