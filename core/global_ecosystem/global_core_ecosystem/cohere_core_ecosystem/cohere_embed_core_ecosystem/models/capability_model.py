from dataclasses import dataclass
@dataclass(frozen=True)
class CapabilityDescriptor:
    name: str = "embed"
    provider: str = "cohere"
    mode: str = "contract_only"
    live_enabled: bool = False
