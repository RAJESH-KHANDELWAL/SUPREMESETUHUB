"""Schemas for services in global_business_api_ecosystem."""
from pydantic import BaseModel


class EcosystemEntry(BaseModel):
    name: str
    description: str = ""
    status: str = "planned"
