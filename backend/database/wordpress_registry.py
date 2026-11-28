"""
MAIN BASE FOUNDATION
WORDPRESS DATABASE REGISTRY

Registers an existing WordPress database inside the
central database foundation.

IMPORTANT:
- This module DOES NOT modify the original WordPress database.
- This module DOES NOT delete WordPress data.
- This module DOES NOT move WordPress data.
- This module DOES NOT merge WordPress databases.
- It only registers and describes the external WordPress database.

Later layers can use this registry for:
- live database connection
- ownership
- permissions
- hosting
- domain
- website
- WordPress management
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Optional

from .service import DatabaseService


class WordPressDatabaseRegistry:
    """Central registry for external WordPress databases."""

    CORE_WORDPRESS_TABLES = {
        "commentmeta",
        "comments",
        "links",
        "options",
        "postmeta",
        "posts",
        "term_relationships",
        "term_taxonomy",
        "termmeta",
        "terms",
        "usermeta",
        "users",
    }

    def __init__(
        self,
        database_service: Optional[DatabaseService] = None,
    ) -> None:
        self.service = (
            database_service
            or DatabaseService()
        )

    # ------------------------------------------------------------------
    # REGISTRY TABLE
    # ------------------------------------------------------------------

    def initialize(self) -> dict:
        """Create the central WordPress registry table."""

        self.service.initialize()

        self.service.execute(
            """
            CREATE TABLE IF NOT EXISTS wordpress_database_registry (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                wordpress_id TEXT NOT NULL UNIQUE,

                website_id TEXT,

                domain_id TEXT,

                hosting_id TEXT,

                database_name TEXT NOT NULL,

                database_engine TEXT,

                database_host TEXT,

                database_port INTEGER,

                table_prefix TEXT,

                site_url TEXT,

                admin_url TEXT,

                table_count INTEGER DEFAULT 0,

                core_table_count INTEGER DEFAULT 0,

                plugin_table_count INTEGER DEFAULT 0,

                connection_status TEXT
                    NOT NULL DEFAULT 'NOT_CONNECTED',

                sync_status TEXT
                    NOT NULL DEFAULT 'NOT_SYNCED',

                ownership_status TEXT
                    NOT NULL DEFAULT 'UNASSIGNED',

                access_mode TEXT
                    NOT NULL DEFAULT 'MANAGED',

                status TEXT
                    NOT NULL DEFAULT 'REGISTERED',

                metadata TEXT,

                created_at TEXT
                    DEFAULT CURRENT_TIMESTAMP,

                updated_at TEXT
                    DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        return {
            "success": True,
            "status": "REGISTRY_READY",
            "table": "wordpress_database_registry",
        }

    # ------------------------------------------------------------------
    # SQL ANALYSIS
    # ------------------------------------------------------------------

    def analyze_sql_file(
        self,
        sql_file: str,
    ) -> dict:
        """
        Analyze a WordPress SQL dump.

        The SQL dump is only read.
        It is never executed against the central database.
        """

        path = Path(sql_file)

        if not path.exists():
            return {
                "success": False,
                "status": "FILE_NOT_FOUND",
                "file": str(path),
            }

        try:
            content = path.read_text(
                encoding="utf-8",
                errors="ignore",
            )
        except Exception as exc:
            return {
                "success": False,
                "status": "FILE_READ_FAILED",
                "error": str(exc),
            }

        database_name = self._detect_database_name(
            content
        )

        table_names = self._detect_tables(
            content
        )

        prefix = self._detect_prefix(
            table_names
        )

        core_tables = []
        plugin_tables = []

        for table in table_names:
            suffix = table

            if prefix and table.startswith(prefix):
                suffix = table[len(prefix):]

            if suffix in self.CORE_WORDPRESS_TABLES:
                core_tables.append(table)
            else:
                plugin_tables.append(table)

        site_url = self._detect_option(
            content,
            prefix,
            "siteurl",
        )

        home_url = self._detect_option(
            content,
            prefix,
            "home",
        )

        return {
            "success": True,
            "status": "ANALYZED",

            "database_name": database_name,

            "database_engine": "MySQL/MariaDB",

            "table_prefix": prefix,

            "site_url": site_url,

            "home_url": home_url,

            "table_count": len(table_names),

            "core_table_count": len(
                core_tables
            ),

            "plugin_table_count": len(
                plugin_tables
            ),

            "tables": table_names,

            "core_tables": core_tables,

            "plugin_tables": plugin_tables,

            "source_file": str(path),
        }

    # ------------------------------------------------------------------
    # REGISTER
    # ------------------------------------------------------------------

    def register(
        self,
        wordpress_id: str,
        analysis: dict,
        website_id: Optional[str] = None,
        domain_id: Optional[str] = None,
        hosting_id: Optional[str] = None,
        database_host: Optional[str] = None,
        database_port: Optional[int] = None,
    ) -> dict:
        """Register an analyzed WordPress database."""

        self.initialize()

        if not analysis.get("success"):
            return {
                "success": False,
                "status": "INVALID_ANALYSIS",
            }

        existing = self.service.fetchone(
            """
            SELECT id
            FROM wordpress_database_registry
            WHERE wordpress_id = ?
            """,
            (wordpress_id,),
        )

        if existing:
            self.service.execute(
                """
                UPDATE wordpress_database_registry
                SET
                    website_id = ?,
                    domain_id = ?,
                    hosting_id = ?,
                    database_name = ?,
                    database_engine = ?,
                    database_host = ?,
                    database_port = ?,
                    table_prefix = ?,
                    site_url = ?,
                    table_count = ?,
                    core_table_count = ?,
                    plugin_table_count = ?,
                    updated_at = CURRENT_TIMESTAMP
                WHERE wordpress_id = ?
                """,
                (
                    website_id,
                    domain_id,
                    hosting_id,
                    analysis.get(
                        "database_name"
                    ),
                    analysis.get(
                        "database_engine"
                    ),
                    database_host,
                    database_port,
                    analysis.get(
                        "table_prefix"
                    ),
                    analysis.get(
                        "site_url"
                    ),
                    analysis.get(
                        "table_count",
                        0,
                    ),
                    analysis.get(
                        "core_table_count",
                        0,
                    ),
                    analysis.get(
                        "plugin_table_count",
                        0,
                    ),
                    wordpress_id,
                ),
            )

            return {
                "success": True,
                "status": "UPDATED",
                "wordpress_id": wordpress_id,
            }

        self.service.execute(
            """
            INSERT INTO wordpress_database_registry (
                wordpress_id,
                website_id,
                domain_id,
                hosting_id,
                database_name,
                database_engine,
                database_host,
                database_port,
                table_prefix,
                site_url,
                table_count,
                core_table_count,
                plugin_table_count,
                connection_status,
                sync_status,
                ownership_status,
                access_mode,
                status
            )
            VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                wordpress_id,
                website_id,
                domain_id,
                hosting_id,
                analysis.get(
                    "database_name"
                ),
                analysis.get(
                    "database_engine"
                ),
                database_host,
                database_port,
                analysis.get(
                    "table_prefix"
                ),
                analysis.get(
                    "site_url"
                ),
                analysis.get(
                    "table_count",
                    0,
                ),
                analysis.get(
                    "core_table_count",
                    0,
                ),
                analysis.get(
                    "plugin_table_count",
                    0,
                ),
                "NOT_CONNECTED",
                "NOT_SYNCED",
                "UNASSIGNED",
                "MANAGED",
                "REGISTERED",
            ),
        )

        return {
            "success": True,
            "status": "REGISTERED",
            "wordpress_id": wordpress_id,
        }

    # ------------------------------------------------------------------
    # GET
    # ------------------------------------------------------------------

    def get(
        self,
        wordpress_id: str,
    ) -> Optional[dict]:
        """Return one registered WordPress database."""

        row = self.service.fetchone(
            """
            SELECT *
            FROM wordpress_database_registry
            WHERE wordpress_id = ?
            """,
            (wordpress_id,),
        )

        if row is None:
            return None

        return dict(row)

    # ------------------------------------------------------------------
    # LIST
    # ------------------------------------------------------------------

    def list_all(self) -> list[dict]:
        """Return all registered WordPress databases."""

        rows = self.service.fetchall(
            """
            SELECT *
            FROM wordpress_database_registry
            ORDER BY id ASC
            """
        )

        return [
            dict(row)
            for row in rows
        ]

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------

    def status(self) -> dict:
        """Return registry status."""

        self.initialize()

        row = self.service.fetchone(
            """
            SELECT COUNT(*) AS count
            FROM wordpress_database_registry
            """
        )

        count = (
            int(row["count"])
            if row
            else 0
        )

        return {
            "success": True,
            "status": "READY",
            "registered_databases": count,
        }

    # ------------------------------------------------------------------
    # INTERNAL HELPERS
    # ------------------------------------------------------------------

    @staticmethod
    def _detect_database_name(
        content: str,
    ) -> Optional[str]:
        """Detect database name from SQL comments."""

        patterns = (
            r"Database:\s*([A-Za-z0-9_\-]+)",
            r"database_name\s*[:=]\s*['\"]([^'\"]+)",
        )

        for pattern in patterns:
            match = re.search(
                pattern,
                content,
                re.IGNORECASE,
            )

            if match:
                return match.group(1)

        return None

    @staticmethod
    def _detect_tables(
        content: str,
    ) -> list[str]:
        """Detect table names from CREATE TABLE statements."""

        patterns = (
            r"CREATE TABLE\s+(?:IF NOT EXISTS\s+)?[`'\"]?([A-Za-z0-9_\-]+)[`'\"]?",
            r"CREATE TABLE\s+(?:IF NOT EXISTS\s+)?`([^`]+)`",
        )

        tables: set[str] = set()

        for pattern in patterns:
            matches = re.findall(
                pattern,
                content,
                re.IGNORECASE,
            )

            for table in matches:
                if table:
                    tables.add(table)

        return sorted(tables)

    @staticmethod
    def _detect_prefix(
        tables: list[str],
    ) -> Optional[str]:
        """Detect the common WordPress table prefix."""

        candidates: dict[str, int] = {}

        for table in tables:
            for core_table in (
                "posts",
                "postmeta",
                "options",
                "users",
                "usermeta",
                "comments",
                "terms",
            ):
                suffix = f"_{core_table}"

                if table.endswith(suffix):
                    prefix = table[
                        : -len(core_table)
                    ]

                    candidates[prefix] = (
                        candidates.get(
                            prefix,
                            0,
                        ) + 1
                    )

        if not candidates:
            return None

        return max(
            candidates,
            key=candidates.get,
        )

    @staticmethod
    def _detect_option(
        content: str,
        prefix: Optional[str],
        option_name: str,
    ) -> Optional[str]:
        """Try to detect a WordPress URL option."""

        if not prefix:
            return None

        table = f"{prefix}options"

        pattern = (
            rf"(?:INSERT INTO\s+[`'\"]?{re.escape(table)}"
            rf"[`'\"]?.*?"
            rf"\b{re.escape(option_name)}\b)"
        )

        if not re.search(
            pattern,
            content,
            re.IGNORECASE | re.DOTALL,
        ):
            return None

        url_pattern = (
            rf"['\"]https?://[^'\"]+['\"]"
        )

        matches = re.findall(
            url_pattern,
            content,
            re.IGNORECASE,
        )

        if matches:
            return (
                matches[0]
                .strip("'\"")
            )

        return None


__all__ = [
    "WordPressDatabaseRegistry",
]
