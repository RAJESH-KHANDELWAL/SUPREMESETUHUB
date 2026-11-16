"""Typed records for creative_commissions work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "creative_commissions"
    taxonomy_status: str = "taxonomy_only"
