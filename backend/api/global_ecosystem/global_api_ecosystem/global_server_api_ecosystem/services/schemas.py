"""Schemas for server service catalog."""
from typing import Any
from pydantic import BaseModel

class ServerServiceEntry(BaseModel):
    name: str
    description: str = ""
    status: str = "catalog_only"
    service_type_id: str
    capabilities: list[str] = []

class ServerServiceCatalog(BaseModel):
    success: bool
    count: int
    services: list[ServerServiceEntry]
