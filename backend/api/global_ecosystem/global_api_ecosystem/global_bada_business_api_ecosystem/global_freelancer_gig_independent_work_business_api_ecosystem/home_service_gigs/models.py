"""Typed records for home_service_gigs work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "home_service_gigs"
    taxonomy_status: str = "taxonomy_only"
