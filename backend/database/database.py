"""Python counterpart of backend/database/database.php.

Provides one lazy, shared connection to the physical SUPREMESETUHUB database.
The four named identities are logical row-scope gates, not separate databases.
This module does not create databases/tables and does not connect on import.
The existing WordPress database remains a separate connection.
"""
from __future__ import annotations

from threading import RLock
from typing import Any

from .gde_connection import (
    IDENTITY_GATES,
    IDENTITIES,
    PRIMARY_IDENTITY,
    GDEDatabaseConnection,
    SupremeDatabaseConfig,
)

_connection_manager: GDEDatabaseConnection | None = None
_connection_lock = RLock()


def supreme_main_database_config() -> SupremeDatabaseConfig:
    """Load central SUPREMESETUHUB credentials from SUPREME_DB_* variables."""
    return SupremeDatabaseConfig.from_environment()


def supreme_main_database_manager() -> GDEDatabaseConnection:
    """Return the process-wide manager for the single central database."""
    global _connection_manager
    with _connection_lock:
        if _connection_manager is None:
            _connection_manager = GDEDatabaseConnection(
                supreme_main_database_config()
            )
        return _connection_manager


def supreme_main_database_connection():
    """Open/reuse the one central MySQL/MariaDB connection."""
    return supreme_main_database_manager().connect()


def supreme_identity_database_connection(identity: str = PRIMARY_IDENTITY):
    """Resolve an identity gate to the shared central connection.

    Callers must include identity_code = the returned identity in every
    identity-owned read/write query. A shared connection alone is not
    row-level authorization.
    """
    supreme_identity_scope(identity)  # Validate before opening the connection.
    return supreme_main_database_connection()


def supreme_identity_scope(identity: str) -> dict[str, str]:
    """Return the mandatory row-scope values for an identity-owned query."""
    if identity not in IDENTITIES:
        raise ValueError(f"Unknown SUPREMESETUHUB identity gate: {identity}")
    return {
        "identity_code": identity,
        "storage_database": "SUPREMESETUHUB",
    }


def supreme_database_health() -> dict[str, Any]:
    """Return a non-secret health result for the central database."""
    return supreme_main_database_manager().health()


def supreme_database_close() -> None:
    """Close the shared connection manager, primarily for process shutdown/tests."""
    global _connection_manager
    with _connection_lock:
        if _connection_manager is not None:
            _connection_manager.close()
            _connection_manager = None


__all__ = [
    "PRIMARY_IDENTITY",
    "IDENTITY_GATES",
    "IDENTITIES",
    "SupremeDatabaseConfig",
    "supreme_main_database_config",
    "supreme_main_database_manager",
    "supreme_main_database_connection",
    "supreme_identity_database_connection",
    "supreme_identity_scope",
    "supreme_database_health",
    "supreme_database_close",
]
