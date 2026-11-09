"""Typed record for one independently addressable freelance work type."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WorkTypeRecord:
    id: str
    name: str
    description: str
    specialization_id: str
    taxonomy_status: str = "taxonomy_only"
