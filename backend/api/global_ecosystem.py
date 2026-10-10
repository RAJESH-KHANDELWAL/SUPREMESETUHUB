"""GLOBAL ECOSYSTEM API."""

from __future__ import annotations

from typing import Any

from backend.engines.global_ecosystem import GlobalEcosystemManager


class GlobalEcosystemAPI:
    """API facade for the GLOBAL ECOSYSTEM engine."""

    def __init__(self) -> None:
        self.engine = GlobalEcosystemManager()

    def status(self) -> dict[str, Any]:
        """Return ecosystem status."""
        return self.engine.status()

    def health(self) -> dict[str, Any]:
        """Return ecosystem health."""
        return self.engine.health()

    def list(self) -> dict[str, Any]:
        """Return all registered ecosystems."""
        return self.engine.list()

    def names(self) -> dict[str, Any]:
        """Return all ecosystem names."""
        return self.engine.names()

    def get(self, ecosystem_id: str) -> dict[str, Any]:
        """Get an ecosystem by ID or exact name."""

        result = self.engine.get(ecosystem_id)

        if result is None:
            return {
                "success": False,
                "ecosystem_id": ecosystem_id,
                "error": "ECOSYSTEM_NOT_FOUND",
            }

        if hasattr(result, "to_dict"):
            result = result.to_dict()

        return {
            "success": True,
            "ecosystem": result,
        }

    def exists(self, ecosystem_id: str) -> bool:
        """Check whether an ecosystem exists."""
        return self.engine.exists(ecosystem_id)

    def tree(self) -> dict[str, Any]:
        """Return the nested ecosystem hierarchy."""
        return self.engine.tree()

    def connection_map(self) -> dict[str, Any]:
        """Return ecosystem relationships."""
        return self.engine.connection_map()


# Backward compatibility for older imports.
EcosystemAPI = GlobalEcosystemAPI
