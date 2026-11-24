"""Shared read-only runtime for WEBSITE CORE domain metadata."""
from __future__ import annotations
from .domain_catalog import get_domain

class WebsiteCoreDomainManager:
    def __init__(self, domain_id: str):
        self.domain_id = str(domain_id).strip().upper()
        if not self.domain_id:
            raise ValueError("WEBSITE_CORE_DOMAIN_ID_REQUIRED")
        if get_domain(self.domain_id) is None:
            raise ValueError(f"UNKNOWN_WEBSITE_CORE_DOMAIN: {self.domain_id}")

    def describe(self) -> dict:
        return {
            "success": True, "ecosystem_id": "GLOBAL-WEBSITE-CORE-ECOSYSTEM",
            "domain": get_domain(self.domain_id), "layer": "CORE",
            "implementation_mode": "SHARED_METADATA_TAXONOMY",
            "remote_operations_enabled": False,
        }
