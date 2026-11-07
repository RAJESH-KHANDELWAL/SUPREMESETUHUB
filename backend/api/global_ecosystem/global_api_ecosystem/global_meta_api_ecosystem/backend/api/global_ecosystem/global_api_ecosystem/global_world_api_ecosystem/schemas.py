"""Pydantic response schemas for Global World discovery."""
from typing import Any
from pydantic import BaseModel


class WorldDomainListResponse(BaseModel):
    success: bool
    ecosystem_id: str
    count: int
    domains: list[dict[str, Any]]
    facets: dict[str, list[str]]


class WorldDomainResponse(BaseModel):
    success: bool
    domain: dict[str, Any]
