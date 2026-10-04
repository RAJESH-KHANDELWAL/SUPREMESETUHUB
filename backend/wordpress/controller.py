"""
MAIN BASE FOUNDATION
WORDPRESS CONTROLLER

Controller layer for WordPress management.

Responsibilities:
- expose WordPress management operations
- keep higher-level code independent
  from WordPressManagementService internals

This module does NOT contain:
- API routes
- API request/response logic
- Core logic
- Engine logic
- authorization logic
- domain logic
- hosting logic
- server logic

Authorization will be handled by its own layer.
"""

from __future__ import annotations

from typing import Optional

from .service import WordPressManagementService


class WordPressController:
    """Controller facade for WordPress management."""

    def __init__(
        self,
        wordpress_service: WordPressManagementService,
    ) -> None:
        self.service = wordpress_service

    # ------------------------------------------------------------------
    # CONNECTION
    # ------------------------------------------------------------------

    def connect(self) -> dict:
        """Connect to the WordPress database."""

        return self.service.connect()

    def disconnect(self) -> dict:
        """Disconnect from the WordPress database."""

        return self.service.disconnect()

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------

    def status(self) -> dict:
        """Return WordPress connection status."""

        return self.service.status()

    def health(self) -> dict:
        """Return WordPress database health."""

        return self.service.health()

    # ------------------------------------------------------------------
    # INFORMATION
    # ------------------------------------------------------------------

    def information(self) -> dict:
        """Return WordPress database information."""

        return self.service.information()

    # ------------------------------------------------------------------
    # TABLES
    # ------------------------------------------------------------------

    def list_tables(self) -> dict:
        """Return all database tables."""

        return self.service.list_tables()

    def list_wordpress_tables(self) -> dict:
        """Return tables using the WordPress prefix."""

        return self.service.list_wordpress_tables()

    def check_core_tables(self) -> dict:
        """Check standard WordPress core tables."""

        return self.service.check_core_tables()

    # ------------------------------------------------------------------
    # SITE
    # ------------------------------------------------------------------

    def site_summary(self) -> dict:
        """Return a complete safe WordPress site summary."""

        return self.service.site_summary()


__all__ = [
    "WordPressController",
]
