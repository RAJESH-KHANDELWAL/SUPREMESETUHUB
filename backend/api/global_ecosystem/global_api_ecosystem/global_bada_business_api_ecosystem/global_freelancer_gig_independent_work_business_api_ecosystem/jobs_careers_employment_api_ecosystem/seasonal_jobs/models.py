"""Typed Seasonal Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class SeasonalJobTrack:
 id:str
 name:str
 description:str
