"""
MAIN BASE FOUNDATION
WORDPRESS MANAGEMENT SERVICE

WordPress-specific management layer.

Responsibilities:
- WordPress site information
- database health
- database information
- table discovery
- WordPress site status
- safe database inspection

This module does NOT contain:
- API routing
- API request/response handling
- Core engine logic
- authorization logic
- hosting logic
- domain logic
- server logic

Those responsibilities remain in their respective modules.
"""

from __future__ import annotations

from typing import Any, Optional

from ..database.wordpress_connection import (
    WordPressDatabaseConnection,
)


class WordPressManagementService:
    """Management service for a registered WordPress website."""

    def __init__(
        self,
        connection: WordPressDatabaseConnection,
    ) -> None:
        self.connection = connection

    # ------------------------------------------------------------------
    # CONNECTION
    # ------------------------------------------------------------------

    def connect(self) -> dict:
        """Connect to the WordPress database."""

        return self.connection.connect()

    def disconnect(self) -> dict:
        """Disconnect from the WordPress database."""

        return self.connection.disconnect()

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------

    def status(self) -> dict:
        """Return WordPress database connection status."""

        return self.connection.status()

    def health(self) -> dict:
        """Return WordPress database health."""

        return self.connection.health()

    # ------------------------------------------------------------------
    # INFORMATION
    # ------------------------------------------------------------------

    def information(self) -> dict:
        """Return WordPress database information."""

        return self.connection.information()

    # ------------------------------------------------------------------
    # TABLE MANAGEMENT
    # ------------------------------------------------------------------

    def list_tables(self) -> dict:
        """
        Return all tables belonging to the connected
        WordPress database.

        This operation is read-only.
        """

        return self.connection.list_tables()

    # ------------------------------------------------------------------
    # WORDPRESS TABLE CHECK
    # ------------------------------------------------------------------

    def check_core_tables(self) -> dict:
        """
        Check whether the standard WordPress tables exist.

        No table is created, modified, moved, merged, or deleted.
        """

        result = self.connection.list_tables()

        if not result.get("success"):
            return result

        tables = set(
            result.get("tables", [])
        )

        prefix = self.connection.table_prefix

        expected_tables = {
            f"{prefix}commentmeta",
            f"{prefix}comments",
            f"{prefix}links",
            f"{prefix}options",
            f"{prefix}postmeta",
            f"{prefix}posts",
            f"{prefix}term_relationships",
            f"{prefix}term_taxonomy",
            f"{prefix}termmeta",
            f"{prefix}terms",
            f"{prefix}usermeta",
            f"{prefix}users",
        }

        present = sorted(
            expected_tables.intersection(
                tables
            )
        )

        missing = sorted(
            expected_tables.difference(
                tables
            )
        )

        return {
            "success": True,
            "status": "CORE_TABLE_CHECKED",
            "prefix": prefix,
            "expected": len(expected_tables),
            "present": len(present),
            "missing": len(missing),
            "present_tables": present,
            "missing_tables": missing,
            "complete": len(missing) == 0,
        }

    # ------------------------------------------------------------------
    # WORDPRESS TABLE FILTER
    # ------------------------------------------------------------------

    def list_wordpress_tables(self) -> dict:
        """
        Return tables using the configured WordPress prefix.

        This does not modify the database.
        """

        result = self.connection.list_tables()

        if not result.get("success"):
            return result

        prefix = self.connection.table_prefix

        tables = [
            table
            for table in result.get(
                "tables",
                [],
            )
            if table.startswith(prefix)
        ]

        return {
            "success": True,
            "status": "WORDPRESS_TABLES_LISTED",
            "prefix": prefix,
            "count": len(tables),
            "tables": tables,
        }

    # ------------------------------------------------------------------
    # SITE SUMMARY
    # ------------------------------------------------------------------

    def site_summary(self) -> dict:
        """
        Return a safe summary of the connected
        WordPress installation.
        """

        connection_status = (
            self.connection.status()
        )

        health = (
            self.connection.health()
        )

        information = (
            self.connection.information()
            if health.get("success")
            else {
                "success": False,
                "status": "INFORMATION_UNAVAILABLE",
            }
        )

        tables = (
            self.connection.list_tables()
            if health.get("success")
            else {
                "success": False,
                "tables": [],
                "count": 0,
            }
        )

        core = (
            self.check_core_tables()
            if health.get("success")
            else {
                "success": False,
            }
        )

        return {
            "success": True,
            "status": "WORDPRESS_SUMMARY_READY",

            "connection": connection_status,

            "health": health,

            "database": information,

            "tables": {
                "count": tables.get(
                    "count",
                    0,
                ),
            },

            "core_wordpress": core,
        }


__all__ = [
    "WordPressManagementService",
]
