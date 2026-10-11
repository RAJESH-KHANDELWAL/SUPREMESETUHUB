"""Schemas for the platforms area of GLOBAL SYSTEM API ECOSYSTEM."""

from pydantic import BaseModel


class PlatformEntry(BaseModel):
    name: str
    description: str = ""
