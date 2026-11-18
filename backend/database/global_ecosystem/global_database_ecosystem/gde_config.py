"""Python counterpart of gde-config.php.

The GDE configuration is a facade over the canonical central configuration;
it does not create or describe a second physical database.
"""
from __future__ import annotations

from typing import Any

from backend.database.global_ecosystem.global_database_ecosystem.config import (
    global_database_ecosystem_config,
)


def gde_config() -> dict[str, Any]:
    """Return the Global Database Ecosystem configuration."""
    return global_database_ecosystem_config()


__all__ = ["gde_config"]
