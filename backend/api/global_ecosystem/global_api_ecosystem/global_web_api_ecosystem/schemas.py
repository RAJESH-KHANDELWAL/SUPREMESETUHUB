"""Pydantic schemas for GLOBAL WEB API ECOSYSTEM."""

from pydantic import BaseModel


class EcosystemStatus(BaseModel):
    ecosystem: str
    status: str
