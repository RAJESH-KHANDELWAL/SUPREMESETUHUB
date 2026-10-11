"""SUPREME ECOSYSTEM — domain entry point inside the MAIN SUPREME package.

This module is the central domain facade for the ecosystem. The HTTP router
lives in backend.api.supreme_ecosystem; this module owns ecosystem identity
and module metadata so the API layer remains an adapter rather than the
architectural parent of the system.

SUPREME ECOSYSTEM is a child of MAIN SUPREME and inherits its private,
owner-controlled architecture. Public platform authentication must not make
this private owner system public.
"""

from __future__ import annotations

from typing import Final

SYSTEM_NAME: Final[str] = "SUPREME ECOSYSTEM"
PARENT_SYSTEM: Final[str] = "MAIN SUPREME"
ACCESS_POLICY: Final[str] = "PRIVATE_BY_DEFAULT"

CORE_MODULES: Final[tuple[str, ...]] = (
    "IDENTITY",
    "ACCOUNT",
    "DASHBOARD",
    "PROFILE",
    "CONNECTORS",
    "INTEGRATIONS",
    "OWNERSHIP",
    "VAULT",
)


class SupremeEcosystem:
    """Central metadata and capability entry point for SUPREME ECOSYSTEM."""

    name: Final[str] = SYSTEM_NAME
    parent: Final[str] = PARENT_SYSTEM
    access_policy: Final[str] = ACCESS_POLICY
    core_modules: Final[tuple[str, ...]] = CORE_MODULES

    @classmethod
    def status(cls) -> dict[str, object]:
        """Return system identity without implying provider connectivity."""
        return {
            "success": True,
            "system": cls.name,
            "parent": cls.parent,
            "privacy": cls.access_policy,
            "modules": list(cls.core_modules),
        }


supreme_ecosystem = SupremeEcosystem()

__all__ = [
    "ACCESS_POLICY",
    "CORE_MODULES",
    "PARENT_SYSTEM",
    "SYSTEM_NAME",
    "SupremeEcosystem",
    "supreme_ecosystem",
]
