"""Typed records for business_consulting work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "business_consulting"
    taxonomy_status: str = "taxonomy_only"
