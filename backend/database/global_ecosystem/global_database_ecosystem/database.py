"""Python counterpart of the GDE PHP database entry point.

Global Database Ecosystem is a compatibility/service layer over the single
central SUPREMESETUHUB database; it does not open a second physical database.
"""
from __future__ import annotations

from typing import Any

from ...database import (
    PRIMARY_IDENTITY,
    supreme_database_health,
    supreme_identity_database_connection,
    supreme_identity_scope,
)


def global_database_ecosystem_database():
    """Return the shared central database connection."""
    return supreme_identity_database_connection(PRIMARY_IDENTITY)


def global_database_ecosystem_identity_database(identity: str):
    """Resolve a named logical identity to the same central connection."""
    return supreme_identity_database_connection(identity)


def global_database_ecosystem_scope(identity: str) -> dict[str, str]:
    """Return the mandatory identity_code scope for GDE-owned records."""
    return supreme_identity_scope(identity)


def global_database_ecosystem_status() -> dict[str, Any]:
    """Return non-secret GDE topology and connection-health information."""
    health = supreme_database_health()
    return {
        "layer": "GLOBAL_DATABASE_ECOSYSTEM",
        "parent": "SUPREMESETUHUB",
        "physical_database_count": 1,
        "shares_central_connection": True,
        "database_health": health,
    }


__all__ = [
    "global_database_ecosystem_database",
    "global_database_ecosystem_identity_database",
    "global_database_ecosystem_scope",
    "global_database_ecosystem_status",
]
