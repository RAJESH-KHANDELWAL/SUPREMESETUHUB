"""Typed records for ai_automation work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "ai_automation"
    taxonomy_status: str = "taxonomy_only"
