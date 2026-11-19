"""Schemas for the global VPS API ecosystem."""

from pydantic import BaseModel

class VPSProviderStatus(BaseModel):
    provider_id: str
    provider_name: str
    implementation_status: str = "CATALOG_ONLY"
    live_connection_verified: bool = False
