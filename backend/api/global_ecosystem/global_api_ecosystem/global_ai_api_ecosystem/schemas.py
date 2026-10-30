"""Pydantic response schemas for GLOBAL AI API ECOSYSTEM."""

from pydantic import BaseModel


class EcosystemStatus(BaseModel):
    success: bool
    ecosystem_id: str
    ecosystem_name: str
    version: str
    status: str
    implementation_status: str
    live_connection_verified: bool
    provider_count: int
    timestamp: str


class ProviderRecord(BaseModel):
    provider_id: str
    provider_name: str
    implementation_status: str
    live_connection_verified: bool
