"""Shared read-only runtime for the 19 Global AI Core domains."""
from __future__ import annotations

from typing import Any

from .domain_catalog import AI_DOMAIN_DEFINITIONS, ai_domain_summary, list_ai_domain_inventory


class GlobalAICoreDomainManager:
    """Domain-scoped view over the canonical Global AI provider inventory."""

    def __init__(self, domain_id: str) -> None:
        normalized = str(domain_id).strip().upper()
        if normalized not in AI_DOMAIN_DEFINITIONS:
            raise ValueError("UNKNOWN_GLOBAL_AI_CORE_DOMAIN: " + normalized)
        self.domain_id = normalized
        self.definition = AI_DOMAIN_DEFINITIONS[normalized]

    def status(self) -> dict[str, Any]:
        summary = ai_domain_summary()
        domain = next(item for item in summary["domains"] if item["id"] == self.domain_id)
        return {
            "success": True,
            "domain_id": self.domain_id,
            "name": self.definition,
            "status": "CORE_DOMAIN_AVAILABLE",
            "provider_count": domain["provider_count"],
            "live_connections_verified": 0,
            "api_calls_performed": 0,
        }

    def list_products(self) -> dict[str, Any]:
        items = [
            item for item in list_ai_domain_inventory()
            if item["id"] == self.domain_id
        ]
        providers = items[0]["providers"] if items else []
        return {
            "success": True,
            "domain_id": self.domain_id,
            "count": len(providers),
            "products": providers,
        }

    def get_product(self, provider_id: str) -> dict[str, Any] | None:
        needle = str(provider_id).strip().casefold()
        if not needle:
            return None
        return next(
            (
                provider
                for item in list_ai_domain_inventory()
                if item["id"] == self.domain_id
                for provider in item["providers"]
                if str(provider.get("id", "")).casefold() == needle
            ),
            None,
        )


__all__ = ["GlobalAICoreDomainManager"]
