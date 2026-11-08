"""Pydantic request and response schemas for GLOBAL SERVER API."""
from __future__ import annotations

from typing import Any
from pydantic import BaseModel, ConfigDict, Field


class ServerInventoryCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    server_id: str = Field(min_length=1, max_length=128)
    server_name: str = Field(min_length=1, max_length=200)
    provider_id: str = Field(min_length=1, max_length=80)
    server_type: str = Field(min_length=1, max_length=80)
    server_role: str = Field(min_length=1, max_length=80)
    country: str = Field(min_length=2, max_length=3)
    region: str = Field(min_length=1, max_length=120)
    environment: str = Field(min_length=1, max_length=40)
    endpoint: str | None = Field(default=None, max_length=2048)
    protocol: str | None = Field(default=None, max_length=32)
    metadata: dict[str, Any] = Field(default_factory=dict)


class EcosystemStatus(BaseModel):
    success: bool
    ecosystem: str
    status: str
    provider_count: int
    service_type_count: int
    registered_server_count: int
    live_connections_verified: bool
    persistence_enabled: bool


class ProviderCatalogResponse(BaseModel):
    success: bool
    count: int
    providers: list[dict[str, Any]]


class ServerTypeCatalogResponse(BaseModel):
    success: bool
    count: int
    service_types: list[dict[str, Any]]


class ServerInventoryResponse(BaseModel):
    success: bool
    count: int
    servers: list[dict[str, Any]]
