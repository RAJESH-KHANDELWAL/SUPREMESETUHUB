"""Typed records for social_media_management work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "social_media_management"
    taxonomy_status: str = "taxonomy_only"
