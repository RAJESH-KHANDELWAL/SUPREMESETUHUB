"""Typed records for web_development work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "web_development"
    taxonomy_status: str = "taxonomy_only"
