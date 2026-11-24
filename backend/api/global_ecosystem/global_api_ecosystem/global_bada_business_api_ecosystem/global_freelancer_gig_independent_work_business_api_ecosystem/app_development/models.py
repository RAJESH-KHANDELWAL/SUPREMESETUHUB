"""Typed records for app_development work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "app_development"
    taxonomy_status: str = "taxonomy_only"
