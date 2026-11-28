"""Pydantic schemas for GLOBAL SERVER API request contracts."""
from __future__ import annotations

from typing import Any
from pydantic import BaseModel, Field


class ServerInventoryCreate(BaseModel):
    """Request model for registering an existing server resource as metadata."""
    class Config:
        extra = "forbid"
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

    def to_core_payload(self) -> dict[str, Any]:
        """Return only CORE ServerIdentity fields; endpoint stays inventory metadata."""
        return {
            "server_id": self.server_id,
            "provider_id": self.provider_id,
            "server_type": self.server_type,
            "server_role": self.server_role,
            "country": self.country,
            "region": self.region,
            "environment": self.environment,
            "metadata": {
                **self.metadata,
                **({"endpoint": self.endpoint} if self.endpoint else {}),
                **({"protocol": self.protocol} if self.protocol else {}),
                "server_name": self.server_name,
            },
        }


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
