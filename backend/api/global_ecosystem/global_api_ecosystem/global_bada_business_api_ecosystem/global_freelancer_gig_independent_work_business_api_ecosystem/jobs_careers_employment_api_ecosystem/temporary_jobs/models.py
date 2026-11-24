"""Typed Temporary Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class TemporaryJobTrack:
 id:str
 name:str
 description:str
