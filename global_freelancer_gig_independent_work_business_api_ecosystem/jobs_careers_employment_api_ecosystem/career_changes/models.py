"""Typed Career Change Opportunities track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class CareerChangeTrack:
 id:str
 name:str
 description:str
