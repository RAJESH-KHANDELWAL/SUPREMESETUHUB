"""Metadata manager for the backend GLOBAL WORDPRESS ECOSYSTEM.

This layer describes the existing WordPress platform implementation. It does
not perform remote WordPress operations or claim a live connection.
"""

from __future__ import annotations

from typing import Any


class GlobalWordPressEcosystemManager:
    """Expose canonical identity and structural readiness metadata."""

    ECOSYSTEM_ID = "GLOBAL-WORDPRESS-ECOSYSTEM"
    NAME = "GLOBAL WORDPRESS ECOSYSTEM"
    LAYER = "BACKEND"
    STATUS = "CATALOG_ONLY"
    IMPLEMENTATION_PATH = "backend/wordpress"

    def status(self) -> dict[str, Any]:
        return {
            "ecosystem_id": self.ECOSYSTEM_ID,
            "name": self.NAME,
            "layer": self.LAYER,
            "status": self.STATUS,
            "implementation_path": self.IMPLEMENTATION_PATH,
            "live_connection_verified": False,
            "remote_operations_enabled": False,
        }

    def health(self) -> dict[str, Any]:
        from pathlib import Path

        root = Path(__file__).resolve().parents[3]
        required = ("controller.py", "service.py", "registry.py", "connection.py")
        checks = {name: (root / name).is_file() for name in required}
        ready = all(checks.values())
        return {
            **self.status(),
            "status": "STRUCTURE_READY" if ready else "STRUCTURE_INCOMPLETE",
            "checks": checks,
            "success": ready,
        }


_manager: GlobalWordPressEcosystemManager | None = None


def get_manager() -> GlobalWordPressEcosystemManager:
    """Return the shared ecosystem manager instance."""
    global _manager
    if _manager is None:
        _manager = GlobalWordPressEcosystemManager()
    return _manager
