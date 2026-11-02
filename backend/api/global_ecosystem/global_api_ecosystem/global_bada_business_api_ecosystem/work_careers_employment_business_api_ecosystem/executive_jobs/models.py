"""Typed Executive Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class ExecutiveJobTrack:
 id:str
 name:str
 description:str
