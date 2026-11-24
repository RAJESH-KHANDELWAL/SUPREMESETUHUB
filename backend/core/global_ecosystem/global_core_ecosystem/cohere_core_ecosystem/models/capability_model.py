from dataclasses import dataclass
@dataclass(frozen=True)
class CapabilityDescriptor:
    name: str
    description: str
    live_enabled: bool = False
