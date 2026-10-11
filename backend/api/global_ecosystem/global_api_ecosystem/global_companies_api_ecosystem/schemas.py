"""Pydantic schemas for GLOBAL COMPANIES API ECOSYSTEM."""

from pydantic import BaseModel


class EcosystemStatus(BaseModel):
    ecosystem: str
    status: str
