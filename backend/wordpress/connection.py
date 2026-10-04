"""
MAIN BASE FOUNDATION
WORDPRESS CONNECTION

Central connection configuration for WordPress sites.

IMPORTANT:
- Live WordPress database remains on the hosting/provider.
- Credentials are NEVER stored in source code.
- GitHub stores the backend code.
- Runtime environment variables provide credentials.
- This module only manages an authorized WordPress database connection.

Architecture:

GITHUB BACKEND
      ↓
WORDPRESS CONNECTION
      ↓
HOSTING DATABASE
      ↓
WORDPRESS SITE
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

import mysql.connector
from mysql.connector import Error


@dataclass
class WordPressConnectionConfig:
    """Configuration required to connect to one WordPress database."""

    site_id: str
    domain: str

    database_host: str
    database_name: str
    database_user: str
    database_password: str

    database_port: int = 3306
    table_prefix: str = "wp_"

    ssl_enabled: bool = True

    @classmethod
    def from_environment(
        cls,
        site_id: str,
        domain: str,
        prefix: str = "WORDPRESS",
    ) -> "WordPressConnectionConfig":
        """
        Load WordPress database configuration from
        environment variables.

        Example:

        WORDPRESS_DB_HOST
        WORDPRESS_DB_NAME
        WORDPRESS_DB_USER
        WORDPRESS_DB_PASSWORD
        WORDPRESS_DB_PORT
        WORDPRESS_TABLE_PREFIX
        """

        host = os.getenv(
            f"{prefix}_DB_HOST"
        )

        name = os.getenv(
            f"{prefix}_DB_NAME"
        )

        user = os.getenv(
            f"{prefix}_DB_USER"
        )

        password = os.getenv(
            f"{prefix}_DB_PASSWORD"
        )

        port = os.getenv(
            f"{prefix}_DB_PORT",
            "3306",
        )

        table_prefix = os.getenv(
            f"{prefix}_TABLE_PREFIX",
            "wp_",
        )

        missing = []

        if not host:
            missing.append(
                f"{prefix}_DB_HOST"
            )

        if not name:
            missing.append(
                f"{prefix}_DB_NAME"
            )

        if not user:
            missing.append(
                f"{prefix}_DB_USER"
            )

        if not password:
            missing.append(
                f"{prefix}_DB_PASSWORD"
            )

        if missing:
            raise RuntimeError(
                "Missing WordPress database "
                "environment variables: "
                + ", ".join(missing)
            )

        return cls(
            site_id=site_id,
            domain=domain,

            database_host=host,
            database_name=name,
            database_user=user,
            database_password=password,

            database_port=int(port),

            table_prefix=table_prefix,
        )


class WordPressDatabaseConnection:
    """
    Authorized MySQL connection to a WordPress database.
    """

    def __init__(
        self,
        config: WordPressConnectionConfig,
    ) -> None:

        self.config = config
        self.connection = None

    # ==============================================================
    # CONNECT
    # ==============================================================

    def connect(self):
        """Open the WordPress database connection."""

        if self.connection is not None:
            return self.connection

        self.connection = mysql.connector.connect(
            host=self.config.database_host,
            port=self.config.database_port,
            database=self.config.database_name,
            user=self.config.database_user,
            password=self.config.database_password,
            connection_timeout=30,
        )

        return self.connection

    # ==============================================================
    # DISCONNECT
    # ==============================================================

    def disconnect(self) -> None:
        """Close the database connection."""

        if self.connection is not None:
            self.connection.close()

        self.connection = None

    # ==============================================================
    # HEALTH
    # ==============================================================

    def health(self) -> dict:
        """Check WordPress database connectivity."""

        try:
            connection = self.connect()

            cursor = connection.cursor()

            cursor.execute(
                "SELECT 1"
            )

            cursor.fetchone()

            cursor.close()

            return {
                "success": True,
                "status": "CONNECTED",

                "site_id": self.config.site_id,
                "domain": self.config.domain,

                "database": self.config.database_name,

                "table_prefix": (
                    self.config.table_prefix
                ),
            }

        except Error as exc:

            return {
                "success": False,
                "status": "CONNECTION_FAILED",

                "site_id": self.config.site_id,
                "domain": self.config.domain,

                "error": str(exc),
            }

    # ==============================================================
    # WORDPRESS TABLE CHECK
    # ==============================================================

    def check_wordpress_tables(self) -> dict:
        """
        Verify that the connected database contains
        essential WordPress tables.
        """

        connection = self.connect()

        cursor = connection.cursor()

        required_tables = [
            "options",
            "posts",
            "users",
            "usermeta",
        ]

        found = []
        missing = []

        for table in required_tables:

            full_table = (
                self.config.table_prefix
                + table
            )

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM information_schema.tables
                WHERE table_schema = %s
                AND table_name = %s
                """,
                (
                    self.config.database_name,
                    full_table,
                ),
            )

            exists = cursor.fetchone()[0] > 0

            if exists:
                found.append(full_table)
            else:
                missing.append(full_table)

        cursor.close()

        return {
            "success": len(missing) == 0,

            "site_id": self.config.site_id,
            "domain": self.config.domain,

            "database": self.config.database_name,

            "found_tables": found,
            "missing_tables": missing,
        }

    # ==============================================================
    # STATUS
    # ==============================================================

    def status(self) -> dict:
        """Return safe connection status."""

        return {
            "service": (
                "WordPressDatabaseConnection"
            ),

            "site_id": self.config.site_id,

            "domain": self.config.domain,

            "database": (
                self.config.database_name
            ),

            "connected": (
                self.connection is not None
            ),

            "table_prefix": (
                self.config.table_prefix
            ),
        }


__all__ = [
    "WordPressConnectionConfig",
    "WordPressDatabaseConnection",
]
