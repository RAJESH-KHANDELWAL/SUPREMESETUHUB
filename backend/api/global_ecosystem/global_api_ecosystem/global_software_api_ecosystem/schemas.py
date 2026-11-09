"""Pydantic schemas for GLOBAL SOFTWARE API ECOSYSTEM."""

from pydantic import BaseModel


class EcosystemStatus(BaseModel):
    ecosystem: str
    status: str
