"""Response schemas for GLOBAL AI API ECOSYSTEM."""
from pydantic import BaseModel


class EcosystemStatus(BaseModel):
    success: bool
    ecosystem_id: str
    ecosystem_name: str
    version: str
    status: str
    implementation_status: str
    runtime_execution_enabled: bool
    provider_count: int
    connected_provider_count: int
    capability_count: int
    service_count: int
    tool_count: int
    integration_count: int
    timestamp: str


class ProviderRecord(BaseModel):
    provider_id: str
    provider_name: str
    provider_type: str
    catalog_path: str
    integration_status: str
    live_connection_verified: bool = False
