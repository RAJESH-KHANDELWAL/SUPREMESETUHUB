"""Python counterpart of gde-database.php."""
from __future__ import annotations

from backend.database.config import PRIMARY_IDENTITY
from backend.database.database import identity_database_connection


def gde_database_connection(identity: str = PRIMARY_IDENTITY):
    """Resolve a GDE identity to the shared SUPREMESETUHUB connection."""
    return identity_database_connection(identity)


__all__ = ["gde_database_connection"]
