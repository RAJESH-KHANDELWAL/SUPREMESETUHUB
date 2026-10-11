"""MAIN SUPREME domain entry point inside the backend package.

SUPREME-specific core, engines, database repositories and storage are kept
inside this package. SUPREME ECOSYSTEM remains a distinct child package.
"""
from __future__ import annotations

from typing import Any

SYSTEM_NAME = "SUPREME"
ACCESS_POLICY = "PRIVATE_BY_DEFAULT"
ECOSYSTEM_PACKAGE = "backend.supreme.supreme_ecosystem"
LAYER_PACKAGES = {
    "core": "backend.supreme.core",
    "engines": "backend.supreme.engines",
    "database": "backend.supreme.database",
    "storage": "backend.supreme.storage",
}


def status() -> dict[str, Any]:
    """Return SUPREME hierarchy metadata without opening databases."""
    return {
        "success": True,
        "system": SYSTEM_NAME,
        "privacy": ACCESS_POLICY,
        "ecosystem_package": ECOSYSTEM_PACKAGE,
        "layers": dict(LAYER_PACKAGES),
        "people_referral_core": "backend.supreme.core.referral_service",
    }


__all__ = ["SYSTEM_NAME", "ACCESS_POLICY", "ECOSYSTEM_PACKAGE", "LAYER_PACKAGES", "status"]
