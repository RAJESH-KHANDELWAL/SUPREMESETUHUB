"""Typed Local Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class LocalJobTrack:
    id: str
    name: str
    description: str
