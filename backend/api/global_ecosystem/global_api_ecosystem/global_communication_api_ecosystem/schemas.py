"""Pydantic response schemas for the Global Communication API Ecosystem."""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class ProviderStatus(BaseModel):
    provider_id: str
    display_name: str
    category: str
    integration_status: str = "not_configured"
    supported_regions: List[str] = Field(default_factory=lambda: ["IN", "GLOBAL"])
    official_api_required: bool = True
    notes: Optional[str] = None


class CategorySummary(BaseModel):
    category_id: str
    display_name: str
    tier: str
    audience: List[str] = Field(default_factory=list)
    providers: List[str] = Field(default_factory=list)
    compliance_controls: List[str] = Field(default_factory=list)


class EcosystemStatus(BaseModel):
    ecosystem_id: str
    version: str
    category_count: int
    provider_count: int
    connected_provider_count: int
    live_messaging_enabled: bool
    integrations: List[ProviderStatus] = Field(default_factory=list)
    safety_controls: Dict[str, Any] = Field(default_factory=dict)
