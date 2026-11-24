"""Typed corporate employer track model."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class CorporateEmployerTrack:
    id: str
    name: str
    description: str
    ownership_sector: str
