"""Typed Experienced Professional Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class ExperiencedJobTrack:
 id:str
 name:str
 description:str
