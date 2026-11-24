"""Typed records for microtasks work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "microtasks"
    taxonomy_status: str = "taxonomy_only"
