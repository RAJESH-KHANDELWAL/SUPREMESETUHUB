"""Typed records for ministry and department recruitment units."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class GovernmentDepartment:
    id: str
    name: str
    parent_ministry: str
    jurisdiction: str
    official_website: str
    recruiting_authority: str
    employment_domains: tuple[str, ...]
    source_status: str = "unverified"
