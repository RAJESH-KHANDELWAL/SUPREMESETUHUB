"""Response schemas for Bada Business provider integration references."""
from pydantic import BaseModel

class IntegrationEntry(BaseModel):
    id: str
    name: str
    package: str
    provider_type: str
    status: str
    api_documentation_verified: bool
    live_connection_verified: bool
    note: str

class IntegrationListResponse(BaseModel):
    success: bool
    count: int
    registry_status: str
    items: list[IntegrationEntry]

class IntegrationDetailResponse(BaseModel):
    success: bool
    integration: IntegrationEntry

class IntegrationStatusResponse(BaseModel):
    success: bool
    structurally_valid: bool
    integration_count: int
    duplicate_ids: list[str]
    api_documentation_verified_count: int
    live_connection_verified_count: int
    registry_status: str
    note: str
