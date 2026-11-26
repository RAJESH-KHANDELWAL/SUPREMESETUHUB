"""Backend-level iOS ecosystem adapter.

The native iOS project remains owned by Backend Foundation. This manager
provides the independent Backend iOS namespace without duplicating project
configuration or claiming that a native build has been verified.
"""

from backend.foundation.global_ecosystem.global_foundation_ecosystem.ios import (
    IOSFoundationManager,
)


class GlobalIOSEcosystemManager:
    """Expose the canonical iOS Foundation project contract."""

    NAME = "GLOBAL IOS ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self, foundation_component=None):
        self._component = foundation_component or IOSFoundationManager()

    def get_component(self):
        return self._component

    def status(self):
        component_status = self._component.status()
        return {
            "name": self.NAME,
            "version": self.VERSION,
            "status": "INTEGRATED",
            "ecosystem": "GLOBAL_IOS_ECOSYSTEM",
            "component_status": component_status.get("status", "UNKNOWN"),
            "build_verified": component_status.get("build_verified", False),
            "project_path": component_status.get("project_path", "backend/mobile/ios"),
        }


def get_manager():
    """Return the backend iOS ecosystem adapter."""
    return GlobalIOSEcosystemManager()


__all__ = ["GlobalIOSEcosystemManager", "get_manager"]
