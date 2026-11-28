"""Shared read-only runtime for Anthropic Core domain packages."""
from __future__ import annotations

from typing import Any

from .domain_catalog import DOMAIN_DEFINITIONS, anthropic_domain_summary, list_anthropic_domain_inventory


class AnthropicCoreDomainManager:
    """Domain-scoped inventory manager. No API, auth, storage or execution."""

    DOMAIN_ID = ""

    def __init__(self, domain_id: str | None = None) -> None:
        if domain_id is not None:
            self.DOMAIN_ID = domain_id
        if self.DOMAIN_ID not in DOMAIN_DEFINITIONS:
            raise ValueError(f"UNKNOWN_ANTHROPIC_CORE_DOMAIN: {self.DOMAIN_ID}")
        self._definition = DOMAIN_DEFINITIONS[self.DOMAIN_ID]

    def status(self) -> dict[str, Any]:
        summary = anthropic_domain_summary()
        domain = next(d for d in summary["domains"] if d["domain_id"] == self.DOMAIN_ID)
        return {"success": True, "domain_id": self.DOMAIN_ID, "name": self._definition["name"], "purpose": self._definition["purpose"], "status": "CORE_DOMAIN_AVAILABLE", "offering_count": domain["offering_count"], "live_connections_verified": 0, "api_calls_performed": 0}

    def list_offerings(self) -> dict[str, Any]:
        items = [i for i in list_anthropic_domain_inventory() if i["core_domain_id"] == self.DOMAIN_ID]
        return {"success": True, "domain_id": self.DOMAIN_ID, "count": len(items), "offerings": items}

    def get_offering(self, offering_id: str) -> dict[str, Any] | None:
        needle = offering_id.strip().casefold()
        if not needle:
            return None
        return next((i for i in list_anthropic_domain_inventory() if i["core_domain_id"] == self.DOMAIN_ID and str(i.get("product_id", "")).casefold() == needle), None)


__all__ = ["AnthropicCoreDomainManager"]
