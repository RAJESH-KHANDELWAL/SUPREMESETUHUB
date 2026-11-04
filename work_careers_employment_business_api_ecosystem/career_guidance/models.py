"""Typed Career Guidance track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class CareerGuidanceTrack:
 id:str
 name:str
 description:str
