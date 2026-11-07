"""Typed category record for family_relationships_community."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class CategoryRecord:
    id: str
    name: str
    domain_id: str
    adult_restricted: bool = False
