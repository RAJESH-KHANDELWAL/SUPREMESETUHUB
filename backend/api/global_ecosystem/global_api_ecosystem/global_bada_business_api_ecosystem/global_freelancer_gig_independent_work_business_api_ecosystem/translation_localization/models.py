"""Typed records for translation_localization work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "translation_localization"
    taxonomy_status: str = "taxonomy_only"
