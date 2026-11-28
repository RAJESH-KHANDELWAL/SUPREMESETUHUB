"""Typed Public Sector Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class PublicSectorTrack:
    id: str
    name: str
    description: str
