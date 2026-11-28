"""Read-only domain runtime for Cohere Core taxonomy."""
from __future__ import annotations

from typing import Any

from .domain_catalog import DOMAIN_DEFINITIONS, domain_summary, list_domain_inventory


class CohereCoreDomainManager:
    """Read-only manager for one registered Cohere capability domain."""

    def __init__(self, domain_id: str) -> None:
        if not isinstance(domain_id, str) or not domain_id.strip():
            raise ValueError("COHERE_DOMAIN_ID_REQUIRED")
        normalized = domain_id.strip().lower()
        if normalized not in DOMAIN_DEFINITIONS:
            raise KeyError(f"COHERE_DOMAIN_NOT_REGISTERED: {normalized}")
        self.domain_id = normalized

    def get(self) -> dict[str, Any]:
        item = next(row for row in list_domain_inventory() if row["id"] == self.domain_id)
        return {"success": True, **item}

    def capabilities(self) -> dict[str, Any]:
        item = self.get()
        return {"success": True, "domain_id": self.domain_id, "capabilities": item["capabilities"]}

    def status(self) -> dict[str, Any]:
        item = self.get()
        return {
            "success": True,
            "domain_id": self.domain_id,
            "status": "CORE_CATALOG_AVAILABLE",
            "capability_count": item["capability_count"],
            "live_provider_calls_enabled": False,
        }


def get_domain_manager(domain_id: str) -> CohereCoreDomainManager:
    return CohereCoreDomainManager(domain_id)


__all__ = ["CohereCoreDomainManager", "get_domain_manager"]
