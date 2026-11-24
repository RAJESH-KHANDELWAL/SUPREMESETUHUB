"""Typed category record for the adult 18+ lawful industry domain."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class CategoryRecord:
    id: str
    name: str
    domain_id: str
    adult_restricted: bool = False
