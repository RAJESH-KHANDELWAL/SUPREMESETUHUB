"""Typed category record for home_homemaker_care_economy."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class CategoryRecord:
    id: str
    name: str
    domain_id: str
    adult_restricted: bool = False
