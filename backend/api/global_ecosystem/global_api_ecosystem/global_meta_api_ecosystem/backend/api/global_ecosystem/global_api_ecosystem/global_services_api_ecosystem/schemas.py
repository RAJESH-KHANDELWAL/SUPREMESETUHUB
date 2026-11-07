"""Pydantic schemas for GLOBAL SERVICES API ECOSYSTEM."""

from pydantic import BaseModel


class EcosystemStatus(BaseModel):
    ecosystem: str
    status: str
