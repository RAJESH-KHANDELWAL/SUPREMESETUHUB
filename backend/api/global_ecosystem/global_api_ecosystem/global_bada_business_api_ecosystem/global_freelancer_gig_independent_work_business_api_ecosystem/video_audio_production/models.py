"""Typed records for video_audio_production work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "video_audio_production"
    taxonomy_status: str = "taxonomy_only"
