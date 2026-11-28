"""Read-only provider metadata service; never calls provider APIs."""
from __future__ import annotations
from .catalog import get_provider
from .policy import safe_metadata
class ProviderCoreService:
    def __init__(self, provider_id: str):
        self.provider = get_provider(provider_id)
        if self.provider is None: raise LookupError("PROVIDER_NOT_REGISTERED")
    def status(self) -> dict:
        return {"success": True, **safe_metadata(self.provider), "api_calls_performed": 0, "live_connection_verified": False}
    def capabilities(self) -> dict:
        from .catalog import CAPABILITIES
        return {"success": True, "provider_id": self.provider["provider_id"], "capabilities": [{"name": c, "authorization_class": "METADATA_ONLY"} for c in CAPABILITIES]}
