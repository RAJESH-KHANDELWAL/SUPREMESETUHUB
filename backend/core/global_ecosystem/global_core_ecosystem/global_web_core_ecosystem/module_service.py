"""Reusable read-only metadata service for provider-specific WEB CORE packages."""
from __future__ import annotations
from .provider_catalog import get_provider
from .domain_catalog import list_domain_inventory

class WebProviderCoreService:
    def __init__(self, provider_id: str):
        self.provider_id = str(provider_id).strip().lower()
        if get_provider(self.provider_id) is None:
            raise ValueError(f"UNKNOWN_WEB_PROVIDER: {self.provider_id}")

    def describe(self) -> dict:
        provider = get_provider(self.provider_id)
        return {"success": True, "provider": provider, "layer": "CORE",
                "domain_count": len(list_domain_inventory()),
                "live_connection_verified": False, "remote_operations_enabled": False}
