"""Bada Business catalog connector.

This connector exposes the repository's canonical resource directory. It does
not authenticate with Bada Business, call an undocumented endpoint, or claim
live account connectivity.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from backend.bada_business_ecosystem.platform_resources import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    LIVE_CONNECTION_VERIFIED,
    OFFICIAL_PUBLIC_API_VERIFIED,
    STATUS,
    get_catalog,
    get_program,
)


class BadaBusinessConnector:
    """Read-only adapter for canonical Bada Business resource metadata."""

    NAME = "bada_business"
    DISPLAY_NAME = "Bada Business"
    CATEGORY = "business_ecosystem"

    def catalog(self) -> dict[str, Any]:
        """Return a defensive copy of the canonical catalog."""
        return deepcopy(get_catalog())

    def links(self) -> list[dict[str, Any]]:
        return self.catalog()["links"]

    def link(self, link_id: str) -> dict[str, Any] | None:
        wanted = link_id.strip().lower()
        return next(
            (item for item in self.links() if item["id"] == wanted),
            None,
        )

    def programs(self) -> list[dict[str, Any]]:
        return list(self.catalog()["programs"].values())

    def program(self, program_id: str) -> dict[str, Any] | None:
        value = get_program(program_id)
        return deepcopy(value) if value is not None else None

    def status(self) -> dict[str, Any]:
        data = self.catalog()
        return {
            "success": True,
            "connector": self.NAME,
            "display_name": self.DISPLAY_NAME,
            "category": self.CATEGORY,
            "status": "CATALOG_AVAILABLE",
            "catalog_status": STATUS,
            "ecosystem_id": ECOSYSTEM_ID,
            "ecosystem_name": ECOSYSTEM_NAME,
            "link_count": data["link_count"],
            "program_count": data["program_count"],
            "authentication": "NOT_CONFIGURED",
            "connection": "NOT_CONNECTED",
            "official_public_api_verified": OFFICIAL_PUBLIC_API_VERIFIED,
            "live_connection_verified": LIVE_CONNECTION_VERIFIED,
        }


bada_business_connector = BadaBusinessConnector()

__all__ = ["BadaBusinessConnector", "bada_business_connector"]
