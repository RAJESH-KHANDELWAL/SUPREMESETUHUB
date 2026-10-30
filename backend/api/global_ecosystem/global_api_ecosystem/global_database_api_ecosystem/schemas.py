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
