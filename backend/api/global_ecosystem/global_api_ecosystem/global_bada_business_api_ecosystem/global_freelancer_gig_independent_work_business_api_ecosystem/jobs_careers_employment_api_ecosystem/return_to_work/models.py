"""Typed Return-to-Work track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class ReturnToWorkTrack:
 id:str
 name:str
 description:str
