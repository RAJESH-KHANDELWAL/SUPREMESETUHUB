"""Bada Business catalog connector.

The connector exposes the repository's canonical resource directory. It does
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
        return next((item for item in self.links() if item["id"] == wanted), None)

    def search_links(self, query: str) -> list[dict[str, Any]]:
        """Search link ID, display name, type, and URL without changing source data."""
        wanted = query.strip().casefold()
        if not wanted:
            return self.links()
        return [
            item for item in self.links()
            if wanted in " ".join(
                str(item.get(field, "")) for field in ("id", "name", "type", "url")
            ).casefold()
        ]

    def programs(self) -> list[dict[str, Any]]:
        return list(self.catalog()["programs"].values())

    def program(self, program_id: str) -> dict[str, Any] | None:
        value = get_program(program_id)
        return deepcopy(value) if value is not None else None

    def search_programs(self, query: str) -> list[dict[str, Any]]:
        """Search program ID, name, and provider-owned catalog text."""
        wanted = query.strip().casefold()
        programs = self.programs()
        if not wanted:
            return programs
        return [
            item for item in programs
            if wanted in " ".join(
                (str(item.get("program_id", "")), str(item.get("name", "")),
                 str(item.get("provider", "")))
            ).casefold()
        ]

    def status(self) -> dict[str, Any]:
        data = self.catalog()
        return {
            "success": True,
            "connector": self.NAME,
            "display_name": self.DISPLAY_NAME,
            "category": self.CATEGORY,
            "status": "CATALOG_ONLY",
            "catalog_status": STATUS,
            "ecosystem_id": ECOSYSTEM_ID,
            "ecosystem_name": ECOSYSTEM_NAME,
            "link_count": data["link_count"],
            "program_count": data["program_count"],
            "authentication": "NOT_CONFIGURED",
            "connection": "NOT_CONNECTED",
            "official_public_api_verified": OFFICIAL_PUBLIC_API_VERIFIED,
            "live_connection_verified": LIVE_CONNECTION_VERIFIED,
            "supported_actions": ["READ_CATALOG", "LOOKUP_LINK", "LOOKUP_PROGRAM", "SEARCH_CATALOG"],
            "unsupported_actions": [
                "PURCHASE", "ENROLLMENT", "PAYMENT", "LEAD_SUBMISSION",
                "ACCOUNT_READ", "ACCOUNT_WRITE",
            ],
        }


bada_business_connector = BadaBusinessConnector()

__all__ = ["BadaBusinessConnector", "bada_business_connector"]
