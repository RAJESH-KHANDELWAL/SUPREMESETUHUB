"""Shared read-only runtime for OpenAI Core domain packages."""
from __future__ import annotations

from typing import Any

from .domain_catalog import DOMAIN_DEFINITIONS, list_openai_domain_inventory, openai_domain_summary


class OpenAICoreDomainManager:
    """Domain-scoped discovery over the canonical OpenAI Core catalog."""

    DOMAIN_ID = ""

    def __init__(self, domain_id: str | None = None) -> None:
        if domain_id is not None:
            self.DOMAIN_ID = domain_id
        if self.DOMAIN_ID not in DOMAIN_DEFINITIONS:
            raise ValueError(f"UNKNOWN_OPENAI_CORE_DOMAIN: {self.DOMAIN_ID}")
        self._definition = DOMAIN_DEFINITIONS[self.DOMAIN_ID]

    def status(self) -> dict[str, Any]:
        summary = openai_domain_summary()
        domain = next(item for item in summary["domains"] if item["domain_id"] == self.DOMAIN_ID)
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "name": self._definition["name"],
            "purpose": self._definition["purpose"],
            "status": "CORE_DOMAIN_AVAILABLE",
            "product_count": domain["product_count"],
            "api_capability_count": domain["api_capability_count"],
            "live_connection_verified": False,
            "api_calls_performed": 0,
        }

    def list_offerings(self) -> dict[str, Any]:
        product_ids = set(self._definition["product_ids"])
        items = [item for item in list_openai_domain_inventory() if item["id"] in product_ids]
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "count": len(items),
            "offerings": items,
            "api_capabilities": list(self._definition["api_capabilities"]),
        }

    def get_offering(self, product_id: str) -> dict[str, Any] | None:
        needle = str(product_id).strip().casefold()
        if not needle:
            return None
        return next(
            (
                item for item in list_openai_domain_inventory()
                if item["id"].casefold() == needle
                and self.DOMAIN_ID in item["domain_ids"]
            ),
            None,
        )


__all__ = ["OpenAICoreDomainManager"]
