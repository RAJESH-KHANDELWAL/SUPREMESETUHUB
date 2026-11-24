"""Typed Job Placement Services track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class PlacementTrack:
 id:str
 name:str
 description:str
