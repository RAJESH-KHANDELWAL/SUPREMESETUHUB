"""Typed response models for relationship and intimacy ecosystem discovery."""

from typing import Literal
from pydantic import BaseModel, Field


class IntimacyCategory(BaseModel):
    category_id: str
    name: str
    description: str
    scope: str
    implementation_status: Literal["CATALOG_ONLY", "ADAPTER_AVAILABLE", "LIVE_VERIFIED"] = "CATALOG_ONLY"
    age_restricted: bool = False
    requires_compliance_review: bool = False


class IntimacyProvider(BaseModel):
    provider_id: str
    name: str
    category_ids: list[str] = Field(default_factory=list)
    official_url: str | None = None
    official_api_docs_url: str | None = None
    implementation_status: Literal["CATALOG_ONLY", "ADAPTER_AVAILABLE", "LIVE_VERIFIED"] = "CATALOG_ONLY"
    live_connection_verified: bool = False
    notes: str = ""


class IntimacyEcosystemStatus(BaseModel):
    success: bool = True
    system: str = "GLOBAL RELATIONSHIP AND INTIMACY API ECOSYSTEM"
    catalog_only: bool = True
    live_connections_verified: bool = False
    category_count: int
    provider_count: int
    safety_scope: list[str]
