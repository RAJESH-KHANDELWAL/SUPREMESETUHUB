"""
MAIN BASE FOUNDATION
WORDPRESS LIVE DATABASE CONNECTION

Safe connection layer for external WordPress MySQL/MariaDB databases.

Responsibilities:
- connection configuration
- connection lifecycle
- health check
- database identity
- table discovery
- read-only inspection

IMPORTANT:
This layer does NOT automatically modify the external WordPress database.
Write operations must be handled by a higher-level permission-controlled
management layer.
"""

from __future__ import annotations

from threading import RLock
from typing import Any, Optional

try:
    import mysql.connector
    from mysql.connector import Error
except ImportError:
    mysql = None
    Error = Exception


class WordPressDatabaseConnection:
    """Manage a live WordPress MySQL/MariaDB connection."""

    def __init__(
        self,
        host: str,
        database: str,
        username: str,
        password: str,
        port: int = 3306,
        table_prefix: str = "wp_",
        connect_timeout: int = 30,
    ) -> None:

        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self.port = port
        self.table_prefix = table_prefix
        self.connect_timeout = connect_timeout

        self._connection: Optional[Any] = None
        self._lock = RLock()

    # ------------------------------------------------------------------
    # CONNECTION
    # ------------------------------------------------------------------

    def connect(self) -> dict:
        """Connect to the external WordPress database."""

        with self._lock:

            if self._connection is not None:
                return {
                    "success": True,
                    "status": "ALREADY_CONNECTED",
                    "database": self.database,
                }

            if mysql is None:
                return {
                    "success": False,
                    "status": "MYSQL_CONNECTOR_NOT_INSTALLED",
                    "database": self.database,
                }

            try:
                self._connection = mysql.connector.connect(
                    host=self.host,
                    port=self.port,
                    database=self.database,
                    user=self.username,
                    password=self.password,
                    connection_timeout=self.connect_timeout,
                )

                return {
                    "success": True,
                    "status": "CONNECTED",
                    "database": self.database,
                    "host": self.host,
                    "port": self.port,
                }

            except Exception as exc:
                self._connection = None

                return {
                    "success": False,
                    "status": "CONNECTION_FAILED",
                    "database": self.database,
                    "error": str(exc),
                }

    # ------------------------------------------------------------------
    # DISCONNECT
    # ------------------------------------------------------------------

    def disconnect(self) -> dict:
        """Close the external database connection."""

        with self._lock:

            if self._connection is None:
                return {
                    "success": True,
                    "status": "ALREADY_DISCONNECTED",
                }

            try:
                self._connection.close()
            finally:
                self._connection = None

            return {
                "success": True,
                "status": "DISCONNECTED",
            }

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------

    def is_connected(self) -> bool:
        """Return connection status."""

        with self._lock:

            if self._connection is None:
                return False

            try:
                return bool(
                    self._connection.is_connected()
                )
            except Exception:
                return False

    def status(self) -> dict:
        """Return safe connection information."""

        return {
            "service": "WordPressDatabaseConnection",
            "database": self.database,
            "host": self.host,
            "port": self.port,
            "table_prefix": self.table_prefix,
            "connected": self.is_connected(),
        }

    # ------------------------------------------------------------------
    # HEALTH
    # ------------------------------------------------------------------

    def health(self) -> dict:
        """Check the live WordPress database."""

        with self._lock:

            if not self.is_connected():
                return {
                    "success": False,
                    "status": "DISCONNECTED",
                    "database": self.database,
                }

            cursor = None

            try:
                cursor = self._connection.cursor()

                cursor.execute(
                    "SELECT 1"
                )

                result = cursor.fetchone()

                return {
                    "success": True,
                    "status": "HEALTHY",
                    "database": self.database,
                    "connected": True,
                    "test_result": result[0]
                    if result
                    else None,
                }

            except Exception as exc:
                return {
                    "success": False,
                    "status": "UNHEALTHY",
                    "database": self.database,
                    "connected": False,
                    "error": str(exc),
                }

            finally:
                if cursor is not None:
                    cursor.close()

    # ------------------------------------------------------------------
    # TABLE DISCOVERY
    # ------------------------------------------------------------------

    def list_tables(self) -> dict:
        """
        Return tables from the connected WordPress database.

        This operation is read-only.
        """

        with self._lock:

            if not self.is_connected():
                return {
                    "success": False,
                    "status": "DISCONNECTED",
                    "tables": [],
                }

            cursor = None

            try:
                cursor = self._connection.cursor()

                cursor.execute(
                    "SHOW TABLES"
                )

                rows = cursor.fetchall()

                tables = [
                    row[0]
                    for row in rows
                ]

                return {
                    "success": True,
                    "status": "TABLES_DISCOVERED",
                    "database": self.database,
                    "table_prefix": self.table_prefix,
                    "count": len(tables),
                    "tables": tables,
                }

            except Exception as exc:
                return {
                    "success": False,
                    "status": "TABLE_DISCOVERY_FAILED",
                    "tables": [],
                    "error": str(exc),
                }

            finally:
                if cursor is not None:
                    cursor.close()

    # ------------------------------------------------------------------
    # DATABASE INFORMATION
    # ------------------------------------------------------------------

    def information(self) -> dict:
        """Return basic database information."""

        with self._lock:

            if not self.is_connected():
                return {
                    "success": False,
                    "status": "DISCONNECTED",
                }

            cursor = None

            try:
                cursor = self._connection.cursor()

                cursor.execute(
                    "SELECT DATABASE()"
                )

                database_row = cursor.fetchone()

                cursor.execute(
                    "SELECT VERSION()"
                )

                version_row = cursor.fetchone()

                return {
                    "success": True,
                    "status": "AVAILABLE",
                    "database": (
                        database_row[0]
                        if database_row
                        else self.database
                    ),
                    "server_version": (
                        version_row[0]
                        if version_row
                        else None
                    ),
                    "host": self.host,
                    "port": self.port,
                    "table_prefix": self.table_prefix,
                }

            except Exception as exc:
                return {
                    "success": False,
                    "status": "INFORMATION_FAILED",
                    "error": str(exc),
                }

            finally:
                if cursor is not None:
                    cursor.close()


__all__ = [
    "WordPressDatabaseConnection",
]
