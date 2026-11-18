"""Schemas for relationship and intimacy service metadata."""
from typing import Literal
from pydantic import BaseModel

class ServiceEntry(BaseModel):
    service_id: str
    name: str
    category_ids: list[str]
    description: str
    audience: str = "adults"
    implementation_status: Literal["CATALOG_ONLY", "AVAILABLE", "LIVE_VERIFIED"] = "CATALOG_ONLY"
    requires_compliance_review: bool = True
