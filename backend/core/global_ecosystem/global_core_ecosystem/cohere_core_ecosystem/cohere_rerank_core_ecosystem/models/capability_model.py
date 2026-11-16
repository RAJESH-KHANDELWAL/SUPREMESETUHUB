from dataclasses import dataclass
@dataclass(frozen=True)
class CapabilityDescriptor:
    name: str = "rerank"
    provider: str = "cohere"
    mode: str = "contract_only"
    live_enabled: bool = False
