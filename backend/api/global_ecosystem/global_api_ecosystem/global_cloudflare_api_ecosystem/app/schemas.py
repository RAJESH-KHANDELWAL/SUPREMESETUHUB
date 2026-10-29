"""Small typed response schemas for the Cloudflare APP scaffold."""
from typing import TypedDict

class EcosystemStatus(TypedDict):
    provider_id: str
    family: str
    implementation_status: str
    live_connection_verified: bool

class Capability(TypedDict):
    id: str
    name: str
    status: str
