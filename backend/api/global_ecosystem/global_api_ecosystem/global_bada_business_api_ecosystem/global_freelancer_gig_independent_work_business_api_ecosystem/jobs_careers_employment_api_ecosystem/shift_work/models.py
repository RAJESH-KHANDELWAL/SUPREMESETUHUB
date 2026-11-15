"""Typed Shift Work track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class ShiftWorkTrack:
 id:str
 name:str
 description:str
