"""Typed Contract Jobs track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class ContractJobTrack:
 id:str
 name:str
 description:str
