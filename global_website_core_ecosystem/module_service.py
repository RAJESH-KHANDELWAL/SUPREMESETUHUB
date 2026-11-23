"""Reusable read-only metadata service for provider-specific WEBSITE CORE packages."""
from __future__ import annotations
from .provider_catalog import get_provider
from .domain_catalog import list_domain_inventory

class WebsiteProviderCoreService:
    def __init__(self, provider_id: str):
        self.provider_id = str(provider_id).strip().lower()
        if get_provider(self.provider_id) is None:
            raise ValueError(f"UNKNOWN_WEBSITE_PROVIDER: {self.provider_id}")

    def describe(self) -> dict:
        return {
            "success": True, "provider": get_provider(self.provider_id), "layer": "CORE",
            "domain_count": len(list_domain_inventory()), "live_connection_verified": False,
            "remote_operations_enabled": False, "api_calls_performed": 0,
        }
