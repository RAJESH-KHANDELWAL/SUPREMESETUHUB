"""Python database facade for global_ecosystem/database.php."""
from __future__ import annotations

from backend.database.database import identity_database_connection
from backend.database.config import PRIMARY_IDENTITY


def global_ecosystem_database(identity: str = PRIMARY_IDENTITY):
    """Return the shared central connection for a validated identity gate."""
    return identity_database_connection(identity)


__all__ = ["global_ecosystem_database"]
