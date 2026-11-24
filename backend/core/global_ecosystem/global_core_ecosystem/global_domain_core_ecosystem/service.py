"""Public Domain Core service facade."""
from .domain_runtime import DomainCoreRuntime
class GlobalDomainCoreService:
    def __init__(self): self.runtime=DomainCoreRuntime()
    def status(self): return self.runtime.status()
