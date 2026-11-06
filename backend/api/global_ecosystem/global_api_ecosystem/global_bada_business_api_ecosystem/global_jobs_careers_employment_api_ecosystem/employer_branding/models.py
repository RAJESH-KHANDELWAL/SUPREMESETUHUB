"""Typed record for a Jobs & Careers industry category."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class IndustryCategoryRecord:
    id: str
    name: str
    subcategories: tuple[str, ...]
    taxonomy_status: str = "taxonomy_scaffold"
