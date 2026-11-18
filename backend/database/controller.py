"""MAIN BASE FOUNDATION database controller.

Controller layer for database operations.

This module provides a stable public facade over DatabaseService.

Responsibilities:
- database lifecycle
- database initialization
- SQL execution
- queries
- transactions
- health
- status

This controller intentionally contains no business logic.

Domain, hosting, website, WordPress, application, user,
customer, storage, authentication, authorization, and other
higher-level logic must remain outside this layer.
"""

from __future__ import annotations

import sqlite3
from typing import Any, Iterable, Optional, Sequence

from .service import DatabaseService


class DatabaseController:
    """Public controller facade for the central database layer."""

    def __init__(
        self,
        database_service: Optional[DatabaseService] = None,
    ) -> None:
        self.service = (
            database_service
            if database_service is not None
            else DatabaseService()
        )

    # ------------------------------------------------------------------
    # LIFECYCLE
    # ------------------------------------------------------------------

    def connect(self) -> dict:
        """Connect to the central database and return status."""

        self.service.connect()
        return self.service.status()

    def disconnect(self) -> dict:
        """Disconnect from the central database."""

        self.service.close()
        return self.service.status()

    def initialize(self) -> dict:
        """Initialize the central database and its schema."""

        return self.service.initialize()

    # ------------------------------------------------------------------
    # EXECUTION
    # ------------------------------------------------------------------

    def execute(
        self,
        query: str,
        parameters: Sequence[Any] | Iterable[Any] = (),
    ) -> int:
        """Execute one SQL statement."""

        cursor = self.service.execute(
            query=query,
            parameters=parameters,
        )
        return cursor.rowcount

    def executemany(
        self,
        query: str,
        parameters: Iterable[Sequence[Any]],
    ) -> int:
        """Execute one SQL statement for multiple parameter sets."""

        cursor = self.service.executemany(
            query=query,
            parameters=parameters,
        )
        return cursor.rowcount

    # ------------------------------------------------------------------
    # QUERIES
    # ------------------------------------------------------------------

    def fetchone(
        self,
        query: str,
        parameters: Sequence[Any] | Iterable[Any] = (),
    ) -> Optional[sqlite3.Row]:
        """Return one database row."""

        return self.service.fetchone(
            query=query,
            parameters=parameters,
        )

    def fetchall(
        self,
        query: str,
        parameters: Sequence[Any] | Iterable[Any] = (),
    ) -> list[sqlite3.Row]:
        """Return all matching database rows."""

        return self.service.fetchall(
            query=query,
            parameters=parameters,
        )

    # ------------------------------------------------------------------
    # TRANSACTIONS
    # ------------------------------------------------------------------

    def begin(self) -> dict:
        """Begin a database transaction."""

        return self.service.begin()

    def commit(self) -> dict:
        """Commit the current database transaction."""

        return self.service.commit()

    def rollback(self) -> dict:
        """Rollback the current database transaction."""

        return self.service.rollback()

    # ------------------------------------------------------------------
    # HEALTH
    # ------------------------------------------------------------------

    def health(self) -> dict:
        """Return central database health information."""

        return self.service.health()

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------

    def status(self) -> dict:
        """Return database controller and service status."""

        return {
            "controller": "DatabaseController",
            "service": self.service.status(),
        }


__all__ = [
    "DatabaseController",
]
