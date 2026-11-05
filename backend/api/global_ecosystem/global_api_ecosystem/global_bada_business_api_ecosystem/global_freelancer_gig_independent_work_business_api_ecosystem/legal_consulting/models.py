"""Typed records for legal_consulting work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "legal_consulting"
    taxonomy_status: str = "taxonomy_only"
