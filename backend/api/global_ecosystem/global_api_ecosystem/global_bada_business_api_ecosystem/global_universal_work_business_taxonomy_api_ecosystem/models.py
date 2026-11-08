"""Immutable taxonomy record contracts."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class TaxonomySector:
    code: str
    id: str
    name: str
    groups: tuple[str, ...]
    adult_restricted: bool = False
