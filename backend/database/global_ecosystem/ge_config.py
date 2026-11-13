"""Python counterpart of ge-config.php.

Returns the Global Ecosystem configuration through the canonical Python
configuration facade. Importing this module has no database side effects.
"""
from __future__ import annotations

from typing import Any

from backend.database.global_ecosystem.config import global_ecosystem_config


def ge_config() -> dict[str, Any]:
    """Return the Global Ecosystem configuration."""
    return global_ecosystem_config()


__all__ = ["ge_config"]
