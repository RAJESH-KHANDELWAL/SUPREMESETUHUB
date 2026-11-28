"""Metadata manager for the frontend GLOBAL WORDPRESS ECOSYSTEM.

This namespace is a frontend-facing structural boundary; it does not implement
backend WordPress database access or remote WordPress operations.
"""

from __future__ import annotations

from typing import Any


class GlobalWordPressEcosystemManager:
    """Expose frontend ecosystem identity and backend integration boundary."""

    ECOSYSTEM_ID = "GLOBAL-WORDPRESS-ECOSYSTEM"
    NAME = "GLOBAL WORDPRESS ECOSYSTEM"
    LAYER = "FRONTEND"
    STATUS = "CATALOG_ONLY"
    BACKEND_IMPLEMENTATION_PATH = (
        "backend/wordpress/global_ecosystem/global_wordpress_ecosystem"
    )

    def status(self) -> dict[str, Any]:
        return {
            "ecosystem_id": self.ECOSYSTEM_ID,
            "name": self.NAME,
            "layer": self.LAYER,
            "status": self.STATUS,
            "backend_implementation_path": self.BACKEND_IMPLEMENTATION_PATH,
            "backend_connection_verified": False,
            "remote_operations_enabled": False,
        }


_manager: GlobalWordPressEcosystemManager | None = None


def get_manager() -> GlobalWordPressEcosystemManager:
    """Return the shared frontend ecosystem manager instance."""
    global _manager
    if _manager is None:
        _manager = GlobalWordPressEcosystemManager()
    return _manager
