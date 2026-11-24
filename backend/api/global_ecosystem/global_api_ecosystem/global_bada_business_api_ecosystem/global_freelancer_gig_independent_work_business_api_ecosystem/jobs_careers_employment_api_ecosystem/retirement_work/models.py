"""Typed Retirement-Age Work track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class RetirementWorkTrack:
 id:str
 name:str
 description:str
