"""Provider-wide immutable capability descriptor."""
from dataclasses import dataclass


@dataclass(frozen=True)
class CapabilityDescriptor:
    name: str
    description: str
    package: str
    domain: str
    live_enabled: bool = False
