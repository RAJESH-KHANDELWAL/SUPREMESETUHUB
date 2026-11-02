"""Pydantic schemas for the Global Server API Ecosystem."""

from pydantic import BaseModel


class EcosystemStatus(BaseModel):
    ecosystem: str
    status: str
