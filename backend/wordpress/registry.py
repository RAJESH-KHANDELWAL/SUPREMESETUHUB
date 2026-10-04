"""
MAIN BASE FOUNDATION
WORDPRESS REGISTRY

Central registry for connected WordPress websites.

Responsibilities:
- register WordPress sites
- store safe site metadata
- identify each WordPress installation
- manage multiple connected sites
- keep site configuration separate
  from database credentials

IMPORTANT:
Database passwords are NOT stored here.

Credentials remain in environment variables
or deployment secrets.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class WordPressSite:
    """Safe metadata for one connected WordPress site."""

    site_id: str
    domain: str

    site_url: Optional[str] = None

    provider: Optional[str] = None

    hosting_account_id: Optional[str] = None

    database_name: Optional[str] = None

    table_prefix: str = "wp_"

    status: str = "REGISTERED"

    environment: str = "production"

    description: Optional[str] = None

    def to_dict(self) -> dict:
        """Return safe site metadata."""

        return asdict(self)


class WordPressRegistry:
    """
    Central registry of WordPress websites.

    This registry is intentionally independent from
    WordPress database credentials.
    """

    def __init__(self) -> None:

        self._sites: dict[
            str,
            WordPressSite
        ] = {}

    # ==============================================================
    # REGISTER
    # ==============================================================

    def register(
        self,
        site: WordPressSite,
    ) -> WordPressSite:
        """Register a WordPress website."""

        if not site.site_id:
            raise ValueError(
                "site_id is required."
            )

        if not site.domain:
            raise ValueError(
                "domain is required."
            )

        if site.site_id in self._sites:
            raise ValueError(
                f"WordPress site already registered: "
                f"{site.site_id}"
            )

        self._sites[
            site.site_id
        ] = site

        return site

    # ==============================================================
    # UPDATE
    # ==============================================================

    def update(
        self,
        site: WordPressSite,
    ) -> WordPressSite:
        """Update an existing WordPress site."""

        if site.site_id not in self._sites:
            raise ValueError(
                f"WordPress site not registered: "
                f"{site.site_id}"
            )

        self._sites[
            site.site_id
        ] = site

        return site

    # ==============================================================
    # GET
    # ==============================================================

    def get(
        self,
        site_id: str,
    ) -> Optional[WordPressSite]:
        """Return one registered WordPress site."""

        return self._sites.get(
            site_id
        )

    # ==============================================================
    # FIND BY DOMAIN
    # ==============================================================

    def find_by_domain(
        self,
        domain: str,
    ) -> Optional[WordPressSite]:
        """Find a WordPress site by domain."""

        normalized = (
            domain
            .lower()
            .strip()
            .replace(
                "https://",
                ""
            )
            .replace(
                "http://",
                ""
            )
            .rstrip("/")
        )

        for site in self._sites.values():

            site_domain = (
                site.domain
                .lower()
                .strip()
                .replace(
                    "https://",
                    ""
                )
                .replace(
                    "http://",
                    ""
                )
                .rstrip("/")
            )

            if site_domain == normalized:
                return site

        return None

    # ==============================================================
    # LIST
    # ==============================================================

    def list_sites(
        self,
    ) -> list[WordPressSite]:
        """Return all registered WordPress sites."""

        return list(
            self._sites.values()
        )

    # ==============================================================
    # REMOVE
    # ==============================================================

    def unregister(
        self,
        site_id: str,
    ) -> bool:
        """Remove a WordPress site from the registry."""

        if site_id not in self._sites:
            return False

        del self._sites[
            site_id
        ]

        return True

    # ==============================================================
    # STATUS
    # ==============================================================

    def set_status(
        self,
        site_id: str,
        status: str,
    ) -> WordPressSite:
        """Update the logical status of a site."""

        site = self.get(
            site_id
        )

        if site is None:
            raise ValueError(
                f"WordPress site not registered: "
                f"{site_id}"
            )

        site.status = status

        return site

    # ==============================================================
    # EXPORT
    # ==============================================================

    def export(
        self,
    ) -> list[dict]:
        """
        Export safe registry data.

        No database passwords or secrets
        are included.
        """

        return [
            site.to_dict()
            for site in self._sites.values()
        ]

    # ==============================================================
    # COUNT
    # ==============================================================

    def count(self) -> int:
        """Return number of registered WordPress sites."""

        return len(
            self._sites
        )

    # ==============================================================
    # HEALTH SUMMARY
    # ==============================================================

    def summary(self) -> dict:
        """Return registry summary."""

        sites = self.list_sites()

        connected = sum(
            1
            for site in sites
            if site.status == "CONNECTED"
        )

        return {
            "registry": "WordPressRegistry",

            "total_sites": len(sites),

            "connected_sites": connected,

            "registered_sites": (
                len(sites) - connected
            ),

            "sites": [
                site.to_dict()
                for site in sites
            ],
        }


__all__ = [
    "WordPressSite",
    "WordPressRegistry",
]
