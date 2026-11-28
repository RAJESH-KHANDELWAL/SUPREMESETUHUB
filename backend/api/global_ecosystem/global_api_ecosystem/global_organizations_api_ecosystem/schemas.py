"""Pydantic response models for the Global Organizations directory."""
from typing import Any
from pydantic import BaseModel, Field

class OrganizationApiStatus(BaseModel):
    ecosystem: str
    status: str
    organization_count: int = 0
    domain_count: int = 0
    organization_type_count: int = 0
    registry_mode: str
    taxonomy_mode: str
    live_external_connections: bool
    note: str

class OrganizationListResponse(BaseModel):
    total: int
    limit: int
    offset: int
    items: list[dict[str, Any]] = Field(default_factory=list)
