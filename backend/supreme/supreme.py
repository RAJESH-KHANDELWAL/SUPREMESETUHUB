"""MAIN SUPREME domain entry point inside the backend package.

This module describes the parent system. Child ecosystem code is kept under
backend.supreme.supreme_ecosystem so it can evolve independently.
"""

from __future__ import annotations

from typing import Any

SYSTEM_NAME = "SUPREME"
ACCESS_POLICY = "PRIVATE_BY_DEFAULT"
ECOSYSTEM_PACKAGE = "backend.supreme.supreme_ecosystem"


def status() -> dict[str, Any]:
    """Return basic parent-system metadata."""
    return {
        "success": True,
        "system": SYSTEM_NAME,
        "privacy": ACCESS_POLICY,
        "ecosystem_package": ECOSYSTEM_PACKAGE,
    }


__all__ = ["SYSTEM_NAME", "ACCESS_POLICY", "ECOSYSTEM_PACKAGE", "status"]
