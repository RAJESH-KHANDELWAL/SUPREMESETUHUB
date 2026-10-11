"""Pydantic schemas for GLOBAL SYSTEM API ECOSYSTEM."""

from pydantic import BaseModel


class EcosystemStatus(BaseModel):
    ecosystem: str
    status: str
