"""Typed records for public recruitment authorities."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class RecruitmentAuthority:
    id: str
    name: str
    authority_type: str
    jurisdiction: str
    official_website: str
    recruitment_scope: tuple[str, ...]
    source_status: str = "unverified"
