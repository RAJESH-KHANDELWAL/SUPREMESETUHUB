"""Schemas for SERVER tools metadata."""
from pydantic import BaseModel

class ServerToolEntry(BaseModel):
    tool_id: str
    name: str
    status: str
    purpose: str

class ServerToolCatalog(BaseModel):
    success: bool
    count: int
    tools: list[ServerToolEntry]
