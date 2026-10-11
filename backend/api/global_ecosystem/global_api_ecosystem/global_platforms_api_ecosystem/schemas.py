"""Pydantic schemas for GLOBAL PLATFORMS API ECOSYSTEM."""

from pydantic import BaseModel


class EcosystemStatus(BaseModel):
    ecosystem: str
    status: str
