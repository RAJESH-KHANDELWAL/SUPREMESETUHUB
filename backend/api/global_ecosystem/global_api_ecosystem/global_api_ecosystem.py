"""Top-level module for the GLOBAL API ECOSYSTEM.

This module provides a small registry of the ecosystem packages in this folder.
Each child ecosystem maintains its own package and same-name Python entry module.
"""

from __future__ import annotations

from typing import Any

ECOSYSTEM_PACKAGES: tuple[str, ...] = (
    "global_app_api_ecosystem",
    "global_business_api_ecosystem",
    "global_server_api_ecosystem",
    "global_software_api_ecosystem",
    "global_system_api_ecosystem",
    "global_web_api_ecosystem",
    "global_website_api_ecosystem",
)


def list_ecosystems() -> list[dict[str, str]]:
    """Return the known top-level ecosystem package names."""
    return [
        {"name": name, "module": f"{name}.{name}"}
        for name in ECOSYSTEM_PACKAGES
    ]


def get_ecosystem(name: str) -> dict[str, Any] | None:
    """Find a registered ecosystem by exact package name."""
    for ecosystem in list_ecosystems():
        if ecosystem["name"] == name:
            return ecosystem
    return None
