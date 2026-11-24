"""Domain Core discovery and orchestration (metadata only)."""
from .domain_runtime import DomainCoreRuntime
class DomainCoreOrchestrator:
    def __init__(self): self.runtime=DomainCoreRuntime()
    def health(self): return self.runtime.status()
    def providers(self): return self.runtime.list_providers()
    def domains(self): return self.runtime.list_domains()
