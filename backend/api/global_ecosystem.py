"""GLOBAL ECOSYSTEM API facade backed by CORE."""

from __future__ import annotations

from typing import Any

from backend.core.global_ecosystem.manager import GlobalEcosystemManager


class GlobalEcosystemAPI:
    """Backward-compatible API facade for GLOBAL ECOSYSTEM."""

    def __init__(self) -> None:
        self.engine = GlobalEcosystemManager()

    def status(self) -> dict[str, Any]:
        return self.engine.status()

    def health(self) -> dict[str, Any]:
        return self.engine.health()

    def list(self) -> dict[str, Any]:
        return self.engine.list()

    def names(self) -> dict[str, Any]:
        return self.engine.names()

    def get(self, ecosystem_id: str) -> dict[str, Any]:
        result = self.engine.get(ecosystem_id)

        if result is None:
            return {
                "success": False,
                "ecosystem_id": ecosystem_id,
                "error": "ECOSYSTEM_NOT_FOUND",
            }

        if isinstance(result, dict) and "success" in result:
            return result

        if hasattr(result, "to_dict"):
            result = result.to_dict()

        return {
            "success": True,
            "ecosystem": result,
        }

    def exists(self, ecosystem_id: str) -> bool:
        return self.engine.exists(ecosystem_id)

    def tree(self) -> dict[str, Any]:
        return self.engine.tree()

    def connection_map(self) -> dict[str, Any]:
        return self.engine.connection_map()


EcosystemAPI = GlobalEcosystemAPI
