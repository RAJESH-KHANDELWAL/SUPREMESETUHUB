"""Typed category record for adult_18_plus_lawful_industry."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class CategoryRecord:
    id: str
    name: str
    domain_id: str
    adult_restricted: bool = False
