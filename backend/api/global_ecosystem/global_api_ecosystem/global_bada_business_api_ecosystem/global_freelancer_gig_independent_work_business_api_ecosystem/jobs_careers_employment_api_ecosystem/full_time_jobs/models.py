"""Typed Full-Time Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class FullTimeJobTrack:
 id:str
 name:str
 description:str
