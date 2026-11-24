"""Schemas for app ecosystem integrations."""
from pydantic import BaseModel


class EcosystemEntry(BaseModel):
    name: str
    description: str = ""
    status: str = "planned"
