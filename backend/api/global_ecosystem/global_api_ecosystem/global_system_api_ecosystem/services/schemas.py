"""Schemas for services."""

from pydantic import BaseModel


class EcosystemEntry(BaseModel):
    name: str
    description: str = ""
