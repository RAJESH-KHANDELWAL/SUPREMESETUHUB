"""Typed API response schemas for the location_restricted_remote_jobs track."""
from typing import TypedDict

class TrackResourceSchema(TypedDict):
    id: str
    category_id: str
    name: str
    description: str
    role_families: list[str]
    taxonomy_status: str
    live_vacancies_available: bool

class TrackStatusSchema(TypedDict):
    success: bool
    category_id: str
    track_id: str
    taxonomy_status: str
    live_vacancies_available: bool
    structurally_valid: bool
