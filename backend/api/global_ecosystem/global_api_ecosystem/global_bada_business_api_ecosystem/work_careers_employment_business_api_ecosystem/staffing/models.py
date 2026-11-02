"""Typed Staffing Services track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class StaffingTrack:
 id:str
 name:str
 description:str
