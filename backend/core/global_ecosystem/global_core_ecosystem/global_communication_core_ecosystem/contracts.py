"""Global Communication Core contracts."""
from typing import TypedDict
class CommunicationProvider(TypedDict):
    provider_id: str
    display_name: str
    category: str
    package: str
    status: str
    live_connection_verified: bool
class CommunicationCoreStatus(TypedDict):
    ecosystem_id: str
    provider_count: int
    connected_provider_count: int
    live_messaging_enabled: bool
