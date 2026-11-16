"""Typed Hybrid Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class HybridJobTrack:
 id:str
 name:str
 description:str
