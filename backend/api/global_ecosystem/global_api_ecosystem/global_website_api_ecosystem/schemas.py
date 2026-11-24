"""Pydantic schemas for GLOBAL WEBSITE API ECOSYSTEM."""

from pydantic import BaseModel


class EcosystemStatus(BaseModel):
    ecosystem: str
    status: str
