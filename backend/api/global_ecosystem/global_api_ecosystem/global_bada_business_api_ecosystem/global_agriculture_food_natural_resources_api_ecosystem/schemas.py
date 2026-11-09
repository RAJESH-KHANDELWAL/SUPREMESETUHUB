"""Pydantic API schemas."""
from pydantic import BaseModel

class EcosystemStatusResponse(BaseModel):
    ecosystem_id: str
    version: str
    status: str
    domain_count: int

class DomainResponse(BaseModel):
    id: str
    name: str
    description: str
    folder: str
    status: str
