"""Stable metadata contracts for communication provider packages."""
from typing import TypedDict
class ProviderContext(TypedDict):
    tenant_id: str
    provider_id: str
    region: str
class ProviderCoreResult(TypedDict):
    provider_id: str
    status: str
    live_connection_verified: bool
    capability_ids: list[str]
