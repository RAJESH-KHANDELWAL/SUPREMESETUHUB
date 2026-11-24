"""Typed Recruitment service track model."""
from dataclasses import dataclass
@dataclass(frozen=True,slots=True)
class RecruitmentTrack:
 id:str
 name:str
 description:str
