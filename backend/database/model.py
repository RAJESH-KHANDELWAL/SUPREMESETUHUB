"""MAIN BASE FOUNDATION database models.

Core data models for the database layer.

This module contains database-level models only.

It intentionally does NOT contain:
- users
- authentication
- authorization
- domains
- hosting
- websites
- WordPress
- business logic
- storage logic
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class DatabaseInfo:
    """Database connection and configuration information."""

    database_path: str
    engine: str = "sqlite"
    version: str = "1.0"
    status: str = "UNKNOWN"
    connected: bool = False
    description: Optional[str] = None

    def to_dict(self) -> dict:
        """Return database information as a dictionary."""

        return {
            "database_path": self.database_path,
            "engine": self.engine,
            "version": self.version,
            "status": self.status,
            "connected": self.connected,
            "description": self.description,
        }


@dataclass
class DatabaseTableInfo:
    """Information about a central database table."""

    name: str
    status: str = "UNKNOWN"
    description: Optional[str] = None

    def to_dict(self) -> dict:
        """Return table information as a dictionary."""

        return {
            "name": self.name,
            "status": self.status,
            "description": self.description,
        }


@dataclass
class DatabaseSchemaInfo:
    """Information about the central database schema."""

    version: str = "1.0"
    status: str = "UNKNOWN"
    table_count: int = 0
    description: Optional[str] = None

    def to_dict(self) -> dict:
        """Return schema information as a dictionary."""

        return {
            "version": self.version,
            "status": self.status,
            "table_count": self.table_count,
            "description": self.description,
        }


__all__ = [
    "DatabaseInfo",
    "DatabaseTableInfo",
    "DatabaseSchemaInfo",
]
