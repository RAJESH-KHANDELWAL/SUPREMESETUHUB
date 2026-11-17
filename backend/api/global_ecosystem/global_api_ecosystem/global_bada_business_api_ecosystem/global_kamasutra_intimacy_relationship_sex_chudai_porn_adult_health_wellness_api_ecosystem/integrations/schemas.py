"""Schemas for relationship and intimacy integration metadata."""
from typing import Literal
from pydantic import BaseModel

class IntegrationEntry(BaseModel):
    integration_id: str
    name: str
    category_ids: list[str]
    description: str
    implementation_status: Literal["CATALOG_ONLY", "ADAPTER_AVAILABLE", "LIVE_VERIFIED"] = "CATALOG_ONLY"
    official_api_required: bool = True
    live_connection_verified: bool = False
    compliance_review_required: bool = True
