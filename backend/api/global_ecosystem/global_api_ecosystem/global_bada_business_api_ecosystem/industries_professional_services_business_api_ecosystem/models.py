"""Typed category record for industries_professional_services."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class CategoryRecord:
    id: str
    name: str
    domain_id: str
    adult_restricted: bool = False
