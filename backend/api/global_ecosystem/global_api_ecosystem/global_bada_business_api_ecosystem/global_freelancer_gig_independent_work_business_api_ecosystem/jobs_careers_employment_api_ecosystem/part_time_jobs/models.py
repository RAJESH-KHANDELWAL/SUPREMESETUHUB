"""Typed Part-Time Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class PartTimeJobTrack:
 id:str
 name:str
 description:str
