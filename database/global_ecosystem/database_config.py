"""Python counterpart of database-config.php in Global Ecosystem."""
from __future__ import annotations

from typing import Any

from backend.database.config import IDENTITIES, main_foundation_config


def database_config() -> dict[str, dict[str, Any]]:
    """Return the five central identity configurations without connecting."""
    databases = main_foundation_config()["databases"]
    return {identity: dict(databases[identity]) for identity in IDENTITIES}


__all__ = ["database_config"]
