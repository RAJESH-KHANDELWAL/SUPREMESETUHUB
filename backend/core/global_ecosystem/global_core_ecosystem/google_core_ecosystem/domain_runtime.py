"""Shared read-only runtime for the 19 Google Core domain packages."""
from __future__ import annotations

from typing import Any

from .domain_catalog import DOMAIN_DEFINITIONS, google_domain_summary, list_google_domain_inventory


class GoogleCoreDomainManager:
    """Domain-scoped view over the canonical Google offering inventory.

    This class performs classification and discovery only. It does not perform
    OAuth, API transport, persistence, billing, or provider-side operations.
    """

    DOMAIN_ID = ""

    def __init__(self, domain_id: str | None = None) -> None:
        if domain_id is not None:
            self.DOMAIN_ID = domain_id
        if self.DOMAIN_ID not in DOMAIN_DEFINITIONS:
            raise ValueError(f"UNKNOWN_GOOGLE_CORE_DOMAIN: {self.DOMAIN_ID}")
        self._definition = DOMAIN_DEFINITIONS[self.DOMAIN_ID]

    def status(self) -> dict[str, Any]:
        summary = google_domain_summary()
        domain = next(
            item for item in summary["domains"]
            if item["domain_id"] == self.DOMAIN_ID
        )
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "name": self._definition["name"],
            "purpose": self._definition["purpose"],
            "status": "CORE_DOMAIN_AVAILABLE",
            "offering_count": domain["offering_count"],
            "live_connections_verified": 0,
            "api_calls_performed": 0,
        }

    def list_offerings(self) -> dict[str, Any]:
        items = [
            item for item in list_google_domain_inventory()
            if item["core_domain_id"] == self.DOMAIN_ID
        ]
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "count": len(items),
            "offerings": items,
        }

    def get_offering(self, offering_id: str) -> dict[str, Any] | None:
        needle = offering_id.strip().casefold()
        if not needle:
            return None
        return next(
            (
                item for item in list_google_domain_inventory()
                if item["core_domain_id"] == self.DOMAIN_ID
                and str(item.get("id", "")).casefold() == needle
            ),
            None,
        )


__all__ = ["GoogleCoreDomainManager"]
