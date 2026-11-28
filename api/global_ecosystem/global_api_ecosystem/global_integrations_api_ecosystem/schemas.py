"""Pydantic schemas for GLOBAL INTEGRATIONS API ECOSYSTEM."""

from pydantic import BaseModel


class EcosystemStatus(BaseModel):
    ecosystem: str
    status: str
