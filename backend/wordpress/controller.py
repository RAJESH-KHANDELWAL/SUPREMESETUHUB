"""
MAIN BASE FOUNDATION
WORDPRESS CONTROLLER

Controller/API-facing layer for WordPress management.

The controller does not contain database logic.

Flow:

FRONTEND / API
      ↓
WORDPRESS CONTROLLER
      ↓
WORDPRESS SERVICE
      ↓
WORDPRESS CONNECTION
      ↓
LIVE WORDPRESS DATABASE
"""

from __future__ import annotations

from typing import Optional

from .registry import WordPressSite
from .service import WordPressService


class WordPressController:
    """Controller facade for the WordPress platform."""

    def __init__(
        self,
        service: Optional[
            WordPressService
        ] = None,
    ) -> None:

        self.service = (
            service
            or WordPressService()
        )

    # ==============================================================
    # SITE MANAGEMENT
    # ==============================================================

    def register_site(
        self,
        site: WordPressSite,
    ) -> WordPressSite:
        """Register a WordPress website."""

        return self.service.register_site(
            site
        )

    def get_site(
        self,
        site_id: str,
    ) -> Optional[WordPressSite]:
        """Return one WordPress website."""

        return self.service.get_site(
            site_id
        )

    def list_sites(
        self,
    ) -> list[WordPressSite]:
        """Return all registered WordPress websites."""

        return self.service.list_sites()

    # ==============================================================
    # DATABASE CONNECTION
    # ==============================================================

    def connect_site(
        self,
        site_id: str,
        environment_prefix: str,
    ) -> dict:
        """Connect a registered WordPress site."""

        return self.service.connect_site(
            site_id=site_id,
            environment_prefix=environment_prefix,
        )

    def disconnect_site(
        self,
        site_id: str,
    ) -> dict:
        """Disconnect a WordPress database."""

        return self.service.disconnect_site(
            site_id
        )

    # ==============================================================
    # HEALTH
    # ==============================================================

    def health(
        self,
        site_id: str,
    ) -> dict:
        """Check live WordPress database health."""

        return self.service.health(
            site_id
        )

    def check_wordpress(
        self,
        site_id: str,
    ) -> dict:
        """Verify essential WordPress tables."""

        return self.service.check_wordpress(
            site_id
        )

    # ==============================================================
    # STATUS
    # ==============================================================

    def connection_status(
        self,
        site_id: str,
    ) -> dict:
        """Return one site's connection status."""

        return self.service.connection_status(
            site_id
        )

    def connection_status_all(
        self,
    ) -> list[dict]:
        """Return connection status for all sites."""

        return self.service.connection_status_all()

    # ==============================================================
    # SUMMARY
    # ==============================================================

    def summary(self) -> dict:
        """Return WordPress platform summary."""

        return self.service.summary()

    def status(self) -> dict:
        """Return controller status."""

        return {
            "controller": "WordPressController",
            "service": self.service.summary(),
        }


__all__ = [
    "WordPressController",
]
