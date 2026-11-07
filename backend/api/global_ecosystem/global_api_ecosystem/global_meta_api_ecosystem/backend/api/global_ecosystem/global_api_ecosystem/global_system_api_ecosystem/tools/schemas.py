"""Schemas for the tools area of GLOBAL SYSTEM API ECOSYSTEM."""

from pydantic import BaseModel


class ToolEntry(BaseModel):
    name: str
    description: str = ""
