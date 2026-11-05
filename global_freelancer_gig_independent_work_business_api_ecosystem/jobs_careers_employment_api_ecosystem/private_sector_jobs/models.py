"""Typed private employer track model."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class PrivateEmployerTrack:
    id: str
    name: str
    description: str
