"""MAIN SUPREME backend entry module.

The implementation package lives in backend.supreme. This module provides
an explicit backend-level entry point while preserving existing package
modules and APIs.
"""

from __future__ import annotations

from typing import Any


SYSTEM_NAME = "SUPREME"
SYSTEM_PACKAGE = "backend.supreme"
ECOSYSTEM_PACKAGE = "backend.supreme.supreme_ecosystem"


def status() -> dict[str, Any]:
    """Return basic SUPREME entry-point metadata."""
    return {
        "success": True,
        "system": SYSTEM_NAME,
        "package": SYSTEM_PACKAGE,
        "ecosystem_package": ECOSYSTEM_PACKAGE,
        "access_policy": "PRIVATE_BY_DEFAULT",
    }


__all__ = ["SYSTEM_NAME", "SYSTEM_PACKAGE", "ECOSYSTEM_PACKAGE", "status"]
