"""Pydantic response models for the global platform ecosystem."""
from typing import Any
from pydantic import BaseModel, Field

class EcosystemStatus(BaseModel):
    ecosystem: str
    status: str
    profile_count: int = 0
    domain_count: int = 0
    platform_type_count: int = 0
    registry_mode: str
    taxonomy_mode: str
    live_external_connections: bool
    note: str

class PlatformListResponse(BaseModel):
    total: int
    limit: int
    offset: int
    include_adult: bool = False
    items: list[dict[str, Any]] = Field(default_factory=list)
