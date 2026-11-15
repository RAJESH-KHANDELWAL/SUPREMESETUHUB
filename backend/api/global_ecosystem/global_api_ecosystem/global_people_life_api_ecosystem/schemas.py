"""Response schemas for the Global People, Work & Life API."""

from typing import Any
from pydantic import BaseModel


class DomainListResponse(BaseModel):
    success: bool
    ecosystem_id: str
    count: int
    domains: list[dict[str, Any]]
    facets: dict[str, list[str]]


class DomainResponse(BaseModel):
    success: bool
    domain: dict[str, Any]
