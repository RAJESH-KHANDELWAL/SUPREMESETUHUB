"""SERVER domain health aggregation."""
from .global_ecosystem.global_server_ecosystem.runtime import runtime_status

class ServerHealthService:
    def __init__(self, registry=None, providers=None):
        self.registry, self.providers = registry, providers
    def health(self):
        return {"domain": "SERVER", "runtime": runtime_status(),
                "inventory": self.registry.status() if self.registry else {"status": "NOT_BOUND"},
                "providers": list(self.providers.catalog()) if self.providers else [],
                "external_connections": "NOT_ATTEMPTED"}
