"""Typed Remote Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class RemoteJobTrack:
    id: str
    name: str
    description: str
