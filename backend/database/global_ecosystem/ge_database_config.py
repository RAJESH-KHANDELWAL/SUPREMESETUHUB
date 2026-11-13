"""Python counterpart of ge-database-config.php."""
from __future__ import annotations

from typing import Any

from backend.database.config import IDENTITIES, main_foundation_config


def ge_database_config() -> dict[str, dict[str, Any]]:
    """Return the five identity connection configurations.

    Every identity maps to the same physical SUPREMESETUHUB database.
    No connection is opened by this configuration function.
    """
    databases = main_foundation_config()["databases"]
    return {identity: dict(databases[identity]) for identity in IDENTITIES}


__all__ = ["ge_database_config"]
