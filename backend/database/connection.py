"""MAIN BASE FOUNDATION database connection.

Compatibility facade for legacy modules. By default, platform modules use
the canonical SUPREME database configured by SUPREME_DB_PATH or
data/supreme.db. An explicit database_name remains an opt-in override for
isolated/test databases or intentional legacy access.
"""
from __future__ import annotations

import os
import sqlite3
from threading import RLock
from typing import Optional

from backend.database.service import DatabaseService


class DatabaseConnection:
    """Compatibility wrapper backed by the canonical DatabaseService."""

    def __init__(
        self,
        database_name: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        # Keep explicit paths working, but eliminate the old implicit
        # main_base_foundation.db split for platform modules.
        self.database_name = (
            database_name
            or os.getenv("SUPREME_DB_PATH")
            or "data/supreme.db"
        )
        self.timeout = timeout
        self._service = DatabaseService(db_path=self.database_name)
        self.connection: Optional[sqlite3.Connection] = None
        self._lock = RLock()

    def connect(self) -> sqlite3.Connection:
        """Return the shared-service SQLite connection."""
        with self._lock:
            if self.connection is not None:
                return self.connection
            connection = self._service.connect()
            connection.execute(
                f"PRAGMA busy_timeout = {max(0, int(self.timeout * 1000))}"
            )
            self.connection = connection
            return connection

    def close(self) -> None:
        """Close this service connection."""
        with self._lock:
            if self.connection is None:
                return
            self._service.close()
            self.connection = None

    def is_connected(self) -> bool:
        with self._lock:
            return self.connection is not None

    def database(self) -> str:
        return self.database_name

    def status(self) -> dict:
        return {
            "database": self.database_name,
            "connected": self.is_connected(),
            "timeout": self.timeout,
        }

    def health(self) -> dict:
        with self._lock:
            if self.connection is None:
                return {
                    "success": False,
                    "status": "DISCONNECTED",
                    "database": self.database_name,
                    "connected": False,
                }
            try:
                self.connection.execute("SELECT 1")
                return {
                    "success": True,
                    "status": "HEALTHY",
                    "database": self.database_name,
                    "connected": True,
                }
            except sqlite3.Error as exc:
                return {
                    "success": False,
                    "status": "UNHEALTHY",
                    "database": self.database_name,
                    "connected": False,
                    "error": str(exc),
                }


__all__ = ["DatabaseConnection"]
