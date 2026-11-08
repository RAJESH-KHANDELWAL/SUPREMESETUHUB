"""MAIN BASE FOUNDATION database schema.

Central schema definitions for the database foundation.

This module defines the central registry tables used to manage:

- system metadata
- infrastructure providers
- domains
- hosting accounts
- websites
- WordPress installations

Provider-neutral design:
Indian, global, normal, premium, reseller, VPS, cloud,
dedicated and other providers can be registered without
changing the database foundation.
"""

from __future__ import annotations

from typing import Any, Dict, List

from .service import DatabaseService


class DatabaseSchema:
    """Manage the CENTRAL DATABASE schema."""

    CORE_TABLES = (
        "system_metadata",
        "providers",
        "domains",
        "hosting_accounts",
        "websites",
        "wordpress_sites",
    )

    def __init__(
        self,
        database_service: DatabaseService | None = None,
    ) -> None:
        self.service = (
            database_service
            or DatabaseService()
        )

    # ------------------------------------------------------------------
    # CREATE
    # ------------------------------------------------------------------

    def create_core_tables(self) -> dict:
        """Create all central database registry tables."""

        self.service.initialize()

        # --------------------------------------------------------------
        # SYSTEM METADATA
        # --------------------------------------------------------------

        self.service.execute(
            """
            CREATE TABLE IF NOT EXISTS system_metadata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT NOT NULL UNIQUE,
                value TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # --------------------------------------------------------------
        # PROVIDERS
        # --------------------------------------------------------------

        self.service.execute(
            """
            CREATE TABLE IF NOT EXISTS providers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                provider_id TEXT NOT NULL UNIQUE,

                provider_name TEXT NOT NULL,

                provider_type TEXT NOT NULL,

                country TEXT,

                region TEXT,

                environment TEXT,

                website TEXT,

                api_endpoint TEXT,

                status TEXT NOT NULL DEFAULT 'REGISTERED',

                authorized INTEGER NOT NULL DEFAULT 0,

                enabled INTEGER NOT NULL DEFAULT 1,

                metadata TEXT,

                created_at TEXT DEFAULT CURRENT_TIMESTAMP,

                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # --------------------------------------------------------------
        # DOMAINS
        # --------------------------------------------------------------

        self.service.execute(
            """
            CREATE TABLE IF NOT EXISTS domains (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                domain_id TEXT NOT NULL UNIQUE,

                domain_name TEXT NOT NULL UNIQUE,

                provider_id TEXT,

                registrar TEXT,

                registration_status TEXT NOT NULL DEFAULT 'PENDING',

                nameserver_status TEXT NOT NULL DEFAULT 'PENDING',

                dns_status TEXT NOT NULL DEFAULT 'PENDING',

                ssl_status TEXT NOT NULL DEFAULT 'PENDING',

                auto_renew INTEGER NOT NULL DEFAULT 1,

                verified INTEGER NOT NULL DEFAULT 0,

                status TEXT NOT NULL DEFAULT 'PENDING',

                metadata TEXT,

                created_at TEXT DEFAULT CURRENT_TIMESTAMP,

                updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (provider_id)
                    REFERENCES providers(provider_id)
                    ON DELETE SET NULL
            )
            """
        )

        # --------------------------------------------------------------
        # HOSTING ACCOUNTS
        # --------------------------------------------------------------

        self.service.execute(
            """
            CREATE TABLE IF NOT EXISTS hosting_accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                hosting_id TEXT NOT NULL UNIQUE,

                provider_id TEXT,

                account_name TEXT,

                plan_name TEXT,

                hosting_type TEXT,

                server_id TEXT,

                control_panel TEXT,

                region TEXT,

                status TEXT NOT NULL DEFAULT 'PENDING',

                verified INTEGER NOT NULL DEFAULT 0,

                metadata TEXT,

                created_at TEXT DEFAULT CURRENT_TIMESTAMP,

                updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (provider_id)
                    REFERENCES providers(provider_id)
                    ON DELETE SET NULL
            )
            """
        )

        # --------------------------------------------------------------
        # WEBSITES
        # --------------------------------------------------------------

        self.service.execute(
            """
            CREATE TABLE IF NOT EXISTS websites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                website_id TEXT NOT NULL UNIQUE,

                domain_id TEXT,

                hosting_id TEXT,

                website_name TEXT,

                website_type TEXT,

                platform TEXT,

                url TEXT,

                status TEXT NOT NULL DEFAULT 'PENDING',

                ssl_enabled INTEGER NOT NULL DEFAULT 0,

                verified INTEGER NOT NULL DEFAULT 0,

                metadata TEXT,

                created_at TEXT DEFAULT CURRENT_TIMESTAMP,

                updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (domain_id)
                    REFERENCES domains(domain_id)
                    ON DELETE SET NULL,

                FOREIGN KEY (hosting_id)
                    REFERENCES hosting_accounts(hosting_id)
                    ON DELETE SET NULL
            )
            """
        )

        # --------------------------------------------------------------
        # WORDPRESS SITES
        # --------------------------------------------------------------

        self.service.execute(
            """
            CREATE TABLE IF NOT EXISTS wordpress_sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                wordpress_id TEXT NOT NULL UNIQUE,

                website_id TEXT,

                domain_id TEXT,

                hosting_id TEXT,

                wordpress_version TEXT,

                php_version TEXT,

                database_engine TEXT,

                database_name TEXT,

                table_prefix TEXT,

                admin_url TEXT,

                site_url TEXT,

                connection_status TEXT NOT NULL DEFAULT 'NOT_CONNECTED',

                sync_status TEXT NOT NULL DEFAULT 'NOT_SYNCED',

                read_only INTEGER NOT NULL DEFAULT 1,

                status TEXT NOT NULL DEFAULT 'ACTIVE',

                metadata TEXT,

                created_at TEXT DEFAULT CURRENT_TIMESTAMP,

                updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (website_id)
                    REFERENCES websites(website_id)
                    ON DELETE SET NULL,

                FOREIGN KEY (domain_id)
                    REFERENCES domains(domain_id)
                    ON DELETE SET NULL,

                FOREIGN KEY (hosting_id)
                    REFERENCES hosting_accounts(hosting_id)
                    ON DELETE SET NULL
            )
            """
        )

        return {
            "success": True,
            "status": "CORE_SCHEMA_READY",
            "tables": list(self.CORE_TABLES),
        }

    # ------------------------------------------------------------------
    # VALIDATION
    # ------------------------------------------------------------------

    def validate(self) -> dict:
        """Validate that all required central tables exist."""

        rows = self.service.fetchall(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            """
        )

        existing = {
            row["name"]
            for row in rows
        }

        missing = [
            table
            for table in self.CORE_TABLES
            if table not in existing
        ]

        return {
            "success": len(missing) == 0,
            "status": (
                "VALID"
                if not missing
                else "INVALID"
            ),
            "required_tables": list(
                self.CORE_TABLES
            ),
            "existing_tables": sorted(
                existing
            ),
            "missing_tables": missing,
        }

    # ------------------------------------------------------------------
    # TABLES
    # ------------------------------------------------------------------

    def tables(self) -> List[str]:
        """Return all database tables."""

        rows = self.service.fetchall(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            ORDER BY name
            """
        )

        return [
            row["name"]
            for row in rows
        ]

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------

    def status(self) -> Dict[str, Any]:
        """Return central database schema status."""

        validation = self.validate()

        return {
            "schema": "DatabaseSchema",
            "status": validation["status"],
            "required_tables": validation[
                "required_tables"
            ],
            "missing_tables": validation[
                "missing_tables"
            ],
        }


__all__ = [
    "DatabaseSchema",
]
