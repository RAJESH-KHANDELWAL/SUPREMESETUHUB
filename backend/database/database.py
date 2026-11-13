"""Python database counterpart to backend/database/database.php.

The central MySQL connection is shared by all five logical identities.
WordPress is a separate connection and is configured for a dedicated
read-only account. No connection is opened merely by importing this module.
"""
from __future__ import annotations

from threading import RLock
from typing import Any

from backend.database.config import (
    IDENTITIES,
    PRIMARY_IDENTITY,
    WordPressDatabaseConfig,
)
from backend.database.gde_connection import (
    GDEDatabaseConnection,
    SupremeDatabaseConnection,
)
from backend.database.wordpress_connection import WordPressDatabaseConnection

_main_connection: GDEDatabaseConnection | None = None
_main_lock = RLock()
_wordpress_connection: WordPressDatabaseConnection | None = None
_wordpress_lock = RLock()


def main_database_connection() -> GDEDatabaseConnection:
    """Return the singleton connection to the one physical central database."""
    global _main_connection
    with _main_lock:
        if _main_connection is None:
            _main_connection = SupremeDatabaseConnection()
        return _main_connection


def identity_database_connection(identity: str = PRIMARY_IDENTITY) -> GDEDatabaseConnection:
    """Resolve an identity gate to the shared central connection.

    This validates identity membership only. Identity-owned queries MUST still
    include an identity_code predicate; sharing a connection is not row isolation.
    """
    if identity not in IDENTITIES:
        raise ValueError(f"Unknown SUPREMESETUHUB identity gate: {identity}")
    return main_database_connection()


def identity_scope(identity: str) -> dict[str, str]:
    if identity not in IDENTITIES:
        raise ValueError(f"Unknown SUPREMESETUHUB identity gate: {identity}")
    return {"identity_code": identity, "database": "SUPREMESETUHUB"}


def wordpress_database_connection() -> WordPressDatabaseConnection:
    """Return a separate WordPress connection using its dedicated read-only user."""
    global _wordpress_connection
    with _wordpress_lock:
        if _wordpress_connection is None:
            config = WordPressDatabaseConfig.from_environment()
            config.validate()
            _wordpress_connection = WordPressDatabaseConnection(
                host=config.host,
                database=config.name,
                username=config.username,
                password=config.password,
                port=config.port,
                table_prefix=config.table_prefix,
                connect_timeout=config.connect_timeout,
            )
        return _wordpress_connection


def close_database_connections() -> None:
    """Close cached connections without changing or migrating any database."""
    global _main_connection, _wordpress_connection
    with _main_lock:
        if _main_connection is not None:
            _main_connection.close()
            _main_connection = None
    with _wordpress_lock:
        if _wordpress_connection is not None:
            _wordpress_connection.disconnect()
            _wordpress_connection = None


__all__ = [
    "GDEDatabaseConnection", "SupremeDatabaseConnection",
    "main_database_connection", "identity_database_connection",
    "identity_scope", "wordpress_database_connection",
    "close_database_connections",
]
