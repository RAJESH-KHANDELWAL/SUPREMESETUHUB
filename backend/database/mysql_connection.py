"""
MAIN BASE FOUNDATION
MySQL Connection Layer

Responsible for connecting SUPREMESETUHUB to external
MySQL databases such as WordPress databases hosted on Hostinger.

This module is separate from the existing SQLite
DatabaseConnection.

IMPORTANT:
- Never hard-code passwords.
- Credentials must come from environment variables.
- Do not store database passwords in GitHub source code.
"""

from __future__ import annotations

import os
from contextlib import contextmanager
from threading import RLock
from typing import Any, Generator, Optional

import pymysql
from pymysql.connections import Connection


class MySQLDatabaseConnection:
    """
    Manage a MySQL connection for external databases.

    Default use case:
        Hostinger WordPress MySQL database
    """

    def __init__(
        self,
        host: Optional[str] = None,
        database: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        port: Optional[int] = None,
        timeout: Optional[float] = None,
    ) -> None:

        self.host = (
            host
            or os.getenv("WORDPRESS_DB_HOST", "")
        )

        self.database_name = (
            database
            or os.getenv("WORDPRESS_DB_NAME", "")
        )

        self.username = (
            username
            or os.getenv("WORDPRESS_DB_USER", "")
        )

        self.password = (
            password
            or os.getenv("WORDPRESS_DB_PASSWORD", "")
        )

        self.port = int(
            port
            or os.getenv(
                "WORDPRESS_DB_PORT",
                "3306",
            )
        )

        self.timeout = float(
            timeout
            or os.getenv(
                "WORDPRESS_DB_TIMEOUT",
                "10",
            )
        )

        self.connection: Optional[
            Connection
        ] = None

        self._lock = RLock()

    # ------------------------------------------------------------------
    # VALIDATION
    # ------------------------------------------------------------------

    def validate_configuration(self) -> None:
        """Validate required MySQL configuration."""

        missing: list[str] = []

        if not self.host:
            missing.append(
                "WORDPRESS_DB_HOST"
            )

        if not self.database_name:
            missing.append(
                "WORDPRESS_DB_NAME"
            )

        if not self.username:
            missing.append(
                "WORDPRESS_DB_USER"
            )

        if not self.password:
            missing.append(
                "WORDPRESS_DB_PASSWORD"
            )

        if missing:
            raise ValueError(
                "Missing MySQL configuration: "
                + ", ".join(missing)
            )

    # ------------------------------------------------------------------
    # CONNECTION
    # ------------------------------------------------------------------

    def connect(self) -> Connection:
        """Create and return an active MySQL connection."""

        with self._lock:

            if self.connection is not None:
                return self.connection

            self.validate_configuration()

            self.connection = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database_name,
                port=self.port,
                connect_timeout=int(
                    self.timeout
                ),
                read_timeout=int(
                    self.timeout
                ),
                write_timeout=int(
                    self.timeout
                ),
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=False,
            )

            return self.connection

    # ------------------------------------------------------------------
    # CLOSE
    # ------------------------------------------------------------------

    def close(self) -> None:
        """Close the active MySQL connection."""

        with self._lock:

            if self.connection is None:
                return

            try:
                self.connection.close()
            finally:
                self.connection = None

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------

    def is_connected(self) -> bool:
        """Return whether a MySQL connection is active."""

        with self._lock:

            if self.connection is None:
                return False

            try:
                self.connection.ping(
                    reconnect=False
                )
                return True

            except Exception:
                return False

    def database(self) -> str:
        """Return the configured database name."""

        return self.database_name

    def status(self) -> dict[str, Any]:
        """Return safe MySQL connection status."""

        return {
            "database": self.database_name,
            "host": self.host,
            "port": self.port,
            "connected": self.is_connected(),
        }

    # ------------------------------------------------------------------
    # HEALTH
    # ------------------------------------------------------------------

    def health(self) -> dict[str, Any]:
        """Check whether the MySQL connection is healthy."""

        with self._lock:

            if self.connection is None:
                return {
                    "success": False,
                    "status": "DISCONNECTED",
                    "database": self.database_name,
                    "connected": False,
                }

            try:

                with self.connection.cursor() as cursor:

                    cursor.execute(
                        "SELECT 1 AS connection_test"
                    )

                    result = cursor.fetchone()

                healthy = bool(
                    result
                    and result.get(
                        "connection_test"
                    ) == 1
                )

                return {
                    "success": healthy,
                    "status": (
                        "HEALTHY"
                        if healthy
                        else "UNHEALTHY"
                    ),
                    "database": self.database_name,
                    "connected": healthy,
                }

            except Exception as exc:

                return {
                    "success": False,
                    "status": "UNHEALTHY",
                    "database": self.database_name,
                    "connected": False,
                    "error": str(exc),
                }

    # ------------------------------------------------------------------
    # DATABASE INFORMATION
    # ------------------------------------------------------------------

    def information(self) -> dict[str, Any]:
        """Return safe information about the connected database."""

        connection = self.connect()

        with connection.cursor() as cursor:

            cursor.execute(
                "SELECT DATABASE() AS database_name"
            )

            database_result = cursor.fetchone()

            cursor.execute(
                "SELECT VERSION() AS mysql_version"
            )

            version_result = cursor.fetchone()

        return {
            "database": (
                database_result.get(
                    "database_name"
                )
                if database_result
                else None
            ),
            "mysql_version": (
                version_result.get(
                    "mysql_version"
                )
                if version_result
                else None
            ),
            "host": self.host,
            "port": self.port,
        }

    # ------------------------------------------------------------------
    # TABLES
    # ------------------------------------------------------------------

    def list_tables(self) -> list[str]:
        """Return all table names from the connected database."""

        connection = self.connect()

        with connection.cursor() as cursor:

            cursor.execute(
                "SHOW TABLES"
            )

            rows = cursor.fetchall()

        tables: list[str] = []

        for row in rows:

            if row:

                value = next(
                    iter(
                        row.values()
                    )
                )

                tables.append(
                    str(value)
                )

        return tables

    # ------------------------------------------------------------------
    # WORDPRESS DETECTION
    # ------------------------------------------------------------------

    def detect_wordpress(
        self,
        table_prefix: str = "wp_",
    ) -> dict[str, Any]:
        """
        Detect whether the connected database
        contains the expected WordPress tables.
        """

        tables = self.list_tables()

        required_tables = [
            f"{table_prefix}options",
            f"{table_prefix}posts",
            f"{table_prefix}users",
            f"{table_prefix}usermeta",
        ]

        found_tables = [
            table
            for table in required_tables
            if table in tables
        ]

        return {
            "wordpress_detected": (
                len(found_tables)
                == len(required_tables)
            ),
            "table_prefix": table_prefix,
            "required_tables": required_tables,
            "found_tables": found_tables,
            "total_tables": len(tables),
        }

    # ------------------------------------------------------------------
    # CONTEXT MANAGER
    # ------------------------------------------------------------------

    @contextmanager
    def session(
        self,
    ) -> Generator[
        Connection,
        None,
        None,
    ]:
        """
        Open a database session.

        Commits on success.
        Rolls back on failure.
        Closes the connection afterwards.
        """

        connection = self.connect()

        try:

            yield connection

            connection.commit()

        except Exception:

            connection.rollback()

            raise

        finally:

            self.close()


__all__ = [
    "MySQLDatabaseConnection",
]
