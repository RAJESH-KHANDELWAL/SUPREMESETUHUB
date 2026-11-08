"""Schemas for relationship and intimacy tool metadata."""
from typing import Literal
from pydantic import BaseModel

class ToolEntry(BaseModel):
    tool_id: str
    name: str
    description: str
    safety_critical: bool = False
    implementation_status: Literal["CATALOG_ONLY", "IMPLEMENTED", "LIVE_VERIFIED"] = "CATALOG_ONLY"
