"""Typed records for seo work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "seo"
    taxonomy_status: str = "taxonomy_only"
