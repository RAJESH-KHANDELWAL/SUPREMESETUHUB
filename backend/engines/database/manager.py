"""
MAIN BASE FOUNDATION
Central Database Engine

Provides persistent SQLite connectivity for MAIN-BASE-FOUNDATION.
Other database URL schemes are reported as unsupported until drivers
and their lifecycle/transaction behavior are implemented.
"""

from datetime import datetime, timezone
import os
from pathlib import Path
import sqlite3
from typing import Optional

from backend.database.service import DatabaseService


class DatabaseEngine:
    """Central database engine for MAIN BASE FOUNDATION."""

    def __init__(
        self,
        database_url: Optional[str] = None,
        timeout: float = 30.0,
    ):
        # Default all platform modules to the canonical SUPREME database.
        if database_url is None:
            configured_path = os.getenv("SUPREME_DB_PATH") or "data/supreme.db"
            database_url = f"sqlite:///{configured_path}"
        self.database_url = database_url
        self.timeout = timeout
        self._status = "READY"
        self.connected = False
        self.last_check = self._now()
        self.connection: Optional[sqlite3.Connection] = None
        self._database_service: Optional[DatabaseService] = None

    def _now(self) -> str:
        """Return current UTC timestamp."""
        return datetime.now(timezone.utc).isoformat()

    def connect(self) -> dict:
        """Connect to SQLite, enabling relational integrity by default."""
        if self.connected and self.connection is not None:
            return self.status()

        if not self.database_url.startswith("sqlite:///"):
            self._status = "UNSUPPORTED"
            self.last_check = self._now()
            raise NotImplementedError(
                "Only SQLite is currently supported by DatabaseEngine."
            )

        database_path = self.database_url[len("sqlite:///"):]

        # Preserve SQLite's in-memory mode instead of creating a file named
        # ':memory:' in the current working directory.
        is_memory = database_path == ":memory:"
        is_uri = database_path.startswith("file:")
        if is_memory:
            target = ":memory:"
        elif is_uri:
            target = database_path
        else:
            path = Path(database_path)
            if not path.is_absolute():
                path = Path.cwd() / path
            path.parent.mkdir(parents=True, exist_ok=True)
            target = str(path)

        connection = None
        try:
            if is_uri:
                # Preserve explicitly configured SQLite URI support.
                connection = sqlite3.connect(
                    target,
                    timeout=self.timeout,
                    check_same_thread=False,
                    uri=True,
                )
                connection.row_factory = sqlite3.Row
                connection.execute("PRAGMA foreign_keys = ON")
                connection.execute(
                    f"PRAGMA busy_timeout = {max(0, int(self.timeout * 1000))}"
                )
            else:
                self._database_service = DatabaseService(db_path=target)
                connection = self._database_service.connect()
                connection.execute(
                    f"PRAGMA busy_timeout = {max(0, int(self.timeout * 1000))}"
                )
            connection.execute("SELECT 1")
        except Exception:
            if connection is not None:
                connection.close()
            self._database_service = None
            self.connection = None
            self.connected = False
            self._status = "ERROR"
            self.last_check = self._now()
            raise

        self.connection = connection
        self.connected = True
        self._status = "CONNECTED"
        self.last_check = self._now()
        return self.status()

    def disconnect(self) -> dict:
        """Disconnect the database engine."""
        if self._database_service is not None:
            self._database_service.close()
            self._database_service = None
        elif self.connection is not None:
            self.connection.close()
        self.connection = None
        self.connected = False
        self._status = "DISCONNECTED"
        self.last_check = self._now()
        return self.status()

    def ensure_connected(self) -> sqlite3.Connection:
        """Return an active database connection."""
        if not self.connected or self.connection is None:
            self.connect()
        if self.connection is None:
            raise RuntimeError("Database connection could not be established.")
        return self.connection

    def execute(self, query: str, parameters: tuple = ()) -> sqlite3.Cursor:
        """Execute a SQL statement and commit it."""
        connection = self.ensure_connected()
        cursor = connection.execute(query, parameters)
        connection.commit()
        self.last_check = self._now()
        return cursor

    def executemany(
        self,
        query: str,
        parameters: list[tuple],
    ) -> sqlite3.Cursor:
        """Execute a SQL statement against multiple parameter sets."""
        connection = self.ensure_connected()
        cursor = connection.executemany(query, parameters)
        connection.commit()
        self.last_check = self._now()
        return cursor

    def fetch_one(
        self,
        query: str,
        parameters: tuple = (),
    ) -> Optional[dict]:
        """Fetch one database record."""
        connection = self.ensure_connected()
        cursor = connection.execute(query, parameters)
        self.last_check = self._now()
        row = cursor.fetchone()
        return dict(row) if row is not None else None

    def fetch_all(
        self,
        query: str,
        parameters: tuple = (),
    ) -> list[dict]:
        """Fetch all database records."""
        connection = self.ensure_connected()
        cursor = connection.execute(query, parameters)
        self.last_check = self._now()
        return [dict(row) for row in cursor.fetchall()]

    def create_table(self, query: str) -> None:
        """Create a database table."""
        self.execute(query)

    def health(self) -> dict:
        """Run a real health query when connected."""
        healthy = False
        if self.connected and self.connection is not None:
            try:
                self.connection.execute("SELECT 1")
                healthy = True
            except sqlite3.Error:
                healthy = False
        return {
            "database": "MAIN BASE FOUNDATION",
            "health": "HEALTHY" if healthy else "NOT_CONNECTED",
            "connected": self.connected and healthy,
            "database_url": self._safe_database_url(),
            "last_check": self.last_check,
        }

    def status(self) -> dict:
        """Return current database status."""
        return {
            "database": "MAIN BASE FOUNDATION",
            "status": self._status,
            "connected": self.connected,
            "database_url": self._safe_database_url(),
            "last_check": self.last_check,
        }

    def ping(self) -> dict:
        """Perform a lightweight database availability check."""
        try:
            connection = self.ensure_connected()
            connection.execute("SELECT 1")
            self.last_check = self._now()
            return {
                "database": "MAIN BASE FOUNDATION",
                "reachable": True,
                "status": "ONLINE",
                "last_check": self.last_check,
            }
        except (sqlite3.Error, NotImplementedError, RuntimeError, OSError):
            self.last_check = self._now()
            return {
                "database": "MAIN BASE FOUNDATION",
                "reachable": False,
                "status": "OFFLINE",
                "last_check": self.last_check,
            }

    def configuration(self) -> dict:
        """Return non-secret configuration and actual driver support status."""
        supported = self.database_url.startswith("sqlite:///")
        return {
            "engine": "DATABASE",
            "database_url": self._safe_database_url(),
            "driver": "SQLITE" if supported else "UNSUPPORTED",
            "requested_driver": self._driver_name(),
            "supported": supported,
            "secret_storage": False,
        }

    def _driver_name(self) -> str:
        """Describe the requested URL scheme without implying it is supported."""
        if self.database_url.startswith("sqlite:///"):
            return "SQLITE"
        if self.database_url.startswith("postgresql://") or self.database_url.startswith("postgres://"):
            return "POSTGRESQL"
        if self.database_url.startswith("mysql://") or self.database_url.startswith("mysql+pymysql://"):
            return "MYSQL"
        return "UNKNOWN"

    def _safe_database_url(self) -> str:
        """Avoid exposing credentials or query-string secrets in diagnostics."""
        value = self.database_url
        if value.startswith("sqlite:///"):
            return value
        if "://" not in value:
            return "[REDACTED]"
        scheme, remainder = value.split("://", 1)
        authority_and_path = remainder.split("?", 1)[0]
        if "@" in authority_and_path:
            credentials, host_path = authority_and_path.rsplit("@", 1)
            username = credentials.split(":", 1)[0]
            safe_authority = f"{username}:***@{host_path}" if username else "***@" + host_path
        else:
            safe_authority = authority_and_path
        suffix = "?[REDACTED]" if "?" in remainder else ""
        return f"{scheme}://{safe_authority}{suffix}"


__all__ = ["DatabaseEngine"]
