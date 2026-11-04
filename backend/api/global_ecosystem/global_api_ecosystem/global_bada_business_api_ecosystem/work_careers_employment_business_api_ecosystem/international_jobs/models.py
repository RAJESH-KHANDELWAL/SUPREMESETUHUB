"""Typed International Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class InternationalJobTrack:
    id: str
    name: str
    description: str
