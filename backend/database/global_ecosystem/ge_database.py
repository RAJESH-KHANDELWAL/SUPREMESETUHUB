"""Python counterpart of ge-database.php."""
from __future__ import annotations

from backend.database.config import PRIMARY_IDENTITY
from backend.database.database import identity_database_connection


def ge_database_connection(identity: str = PRIMARY_IDENTITY):
    """Return the shared central connection for a validated identity gate."""
    return identity_database_connection(identity)


__all__ = ["ge_database_connection"]
