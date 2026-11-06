"""Schemas for app ecosystem services."""
from pydantic import BaseModel


class EcosystemEntry(BaseModel):
    name: str
    description: str = ""
    status: str = "planned"
