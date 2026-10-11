"""Schemas for the companies area of GLOBAL SYSTEM API ECOSYSTEM."""

from pydantic import BaseModel


class CompanieEntry(BaseModel):
    name: str
    description: str = ""
