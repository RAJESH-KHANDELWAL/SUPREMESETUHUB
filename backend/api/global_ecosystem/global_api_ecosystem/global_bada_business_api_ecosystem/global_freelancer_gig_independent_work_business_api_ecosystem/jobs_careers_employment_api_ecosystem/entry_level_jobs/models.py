"""Typed Entry-Level Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class EntryLevelJobTrack:
 id:str
 name:str
 description:str
