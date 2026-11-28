"""Shared read-only runtime for all registered Communication Core domains."""
from __future__ import annotations
from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS, list_domains
from .product_catalog import PROVIDER_DIRECTORY

class CommunicationCoreDomainManager:
    """A domain-scoped discovery facade; never performs provider API calls."""
    def __init__(self, domain_id: str) -> None:
        key = domain_id.strip().upper()
        if key not in DOMAIN_DEFINITIONS:
            raise ValueError(f"UNKNOWN_COMMUNICATION_CORE_DOMAIN: {key}")
        self.domain_id = key
        self.definition = DOMAIN_DEFINITIONS[key]

    def status(self) -> dict[str, Any]:
        return {"success": True, "domain_id": self.domain_id,
                "name": self.definition["name"], "purpose": self.definition["purpose"],
                "status": "CORE_DOMAIN_AVAILABLE", "provider_reference_count": len(PROVIDER_DIRECTORY),
                "live_connections_verified": 0, "api_calls_performed": 0}

    def list_providers(self) -> dict[str, Any]:
        items = [dict(item) for item in PROVIDER_DIRECTORY]
        return {"success": True, "domain_id": self.domain_id,
                "count": len(items), "providers": items,
                "note": "Provider inventory is discovery metadata; domain-specific adapter mapping is not asserted."}

    def list_domains(self) -> dict[str, Any]:
        return {"success": True, "domains": list_domains()}

__all__ = ["CommunicationCoreDomainManager"]
