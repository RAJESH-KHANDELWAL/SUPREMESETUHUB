"""Python counterpart of the Global Ecosystem PHP database entry point.

Global Ecosystem is a logical identity layer over the one physical
SUPREMESETUHUB database. It deliberately reuses the central connection.
"""
from __future__ import annotations

from typing import Any

from ..database import (
    IDENTITY_GATES,
    IDENTITIES,
    PRIMARY_IDENTITY,
    supreme_identity_database_connection,
    supreme_identity_scope,
)


def global_ecosystem_database(identity: str = PRIMARY_IDENTITY):
    """Return the central connection after validating the requested identity."""
    return supreme_identity_database_connection(identity)


def global_ecosystem_scope(identity: str) -> dict[str, str]:
    """Return the mandatory identity_code scope for GE-owned records."""
    return supreme_identity_scope(identity)


def global_ecosystem_identity_gates() -> tuple[str, ...]:
    """List the four logical identity gates."""
    return IDENTITY_GATES


def global_ecosystem_status() -> dict[str, Any]:
    """Describe GE's database topology without exposing credentials."""
    return {
        "layer": "GLOBAL_ECOSYSTEM",
        "parent": "SUPREMESETUHUB",
        "physical_database_count": 1,
        "identity_gates": list(IDENTITY_GATES),
        "shares_central_connection": True,
    }


__all__ = [
    "global_ecosystem_database",
    "global_ecosystem_scope",
    "global_ecosystem_identity_gates",
    "global_ecosystem_status",
    "IDENTITIES",
]
