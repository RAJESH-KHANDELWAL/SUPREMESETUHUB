"""Schemas for the GLOBAL ADULT INDUSTRY ECOSYSTEM catalog."""
from typing import Literal
from pydantic import BaseModel


class AdultIndustryProvider(BaseModel):
    provider_id: str
    name: str
    category: str
    official_website: str
    implementation_status: Literal["CATALOG_ONLY", "DOCUMENTATION_REVIEW", "ADAPTER_IN_PROGRESS", "TESTED"]
    live_connection_verified: bool = False
    notes: str
