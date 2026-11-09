"""Typed records for tutoring work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "tutoring"
    taxonomy_status: str = "taxonomy_only"
