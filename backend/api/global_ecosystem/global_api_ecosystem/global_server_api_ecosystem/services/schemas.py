"""Schemas for services in global_server_api_ecosystem."""
from pydantic import BaseModel


class EcosystemEntry(BaseModel):
    name: str
    description: str = ""
    status: str = "planned"
