"""Pydantic schemas for public taxonomy endpoints only."""
from pydantic import BaseModel

class EcosystemStatusResponse(BaseModel):
    ecosystem_id: str
    version: str
    status: str
    domain_count: int

class DomainResponse(BaseModel):
    id: str
    name: str
    folder: str
    description: str
    status: str
