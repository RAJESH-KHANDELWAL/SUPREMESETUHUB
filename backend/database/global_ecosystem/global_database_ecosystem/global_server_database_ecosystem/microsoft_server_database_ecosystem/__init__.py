"""Microsoft SERVER DATABASE namespace; connection remains opt-in."""
from dataclasses import dataclass

@dataclass(frozen=True)
class MicrosoftServerDatabaseDescriptor:
    provider_id: str = "microsoft"
    domain: str = "SERVER"
    layer: str = "DATABASE"
    implementation_state: str = "ADAPTER_REQUIRED"
    connection_status: str = "NOT_CONFIGURED"
    durable_persistence: bool = False

    def describe(self):
        return {
            "provider_id": self.provider_id,
            "domain": self.domain,
            "layer": self.layer,
            "implementation_state": self.implementation_state,
            "connection_status": self.connection_status,
            "durable_persistence": self.durable_persistence,
        }

__all__ = ["MicrosoftServerDatabaseDescriptor"]
