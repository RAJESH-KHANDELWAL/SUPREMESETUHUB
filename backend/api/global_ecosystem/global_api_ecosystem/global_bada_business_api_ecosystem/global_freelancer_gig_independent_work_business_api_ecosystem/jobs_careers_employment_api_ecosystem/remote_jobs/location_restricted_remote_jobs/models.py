"""Typed response models for the location_restricted_remote_jobs API resource."""
from pydantic import BaseModel, Field

class TrackAPIResource(BaseModel):
    id: str
    category_id: str
    name: str
    description: str
    role_families: list[str] = Field(default_factory=list)
    taxonomy_status: str = "taxonomy_only"
    live_vacancies_available: bool = False

class TrackAPIStatus(BaseModel):
    success: bool = True
    category_id: str
    track_id: str
    taxonomy_status: str = "taxonomy_only"
    live_vacancies_available: bool = False
    structurally_valid: bool = True
