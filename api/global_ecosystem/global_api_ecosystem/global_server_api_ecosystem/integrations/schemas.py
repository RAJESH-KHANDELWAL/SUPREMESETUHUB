"""Schemas for SERVER cross-layer integration metadata."""
from pydantic import BaseModel

class ServerIntegrationEntry(BaseModel):
    integration_id: str
    name: str
    status: str
    direction: str
    purpose: str

class ServerIntegrationCatalog(BaseModel):
    success: bool
    count: int
    integrations: list[ServerIntegrationEntry]
