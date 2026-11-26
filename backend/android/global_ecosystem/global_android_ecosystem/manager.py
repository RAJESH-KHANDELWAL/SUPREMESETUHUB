"""Backend-level Android ecosystem adapter.

The native Android project remains owned by Backend Foundation. This manager
provides the independent Backend Android namespace without duplicating the
project configuration or claiming that a release build has been verified.
"""

from backend.foundation.global_ecosystem.global_foundation_ecosystem.android import (
    AndroidFoundationManager,
)


class GlobalAndroidEcosystemManager:
    """Expose the canonical Android Foundation project contract."""

    NAME = "GLOBAL ANDROID ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self, foundation_component=None):
        self._component = foundation_component or AndroidFoundationManager()

    def get_component(self):
        return self._component

    def project_contract(self):
        return self._component.project_contract()

    def status(self):
        component_status = self._component.status()
        return {
            "name": self.NAME,
            "version": self.VERSION,
            "status": "INTEGRATED",
            "ecosystem": "GLOBAL_ANDROID_ECOSYSTEM",
            "component_status": component_status["status"],
            "build_verified": component_status.get("build_verified", False),
            "project_path": component_status["project_path"],
        }


def get_manager():
    """Return the backend Android ecosystem adapter."""
    return GlobalAndroidEcosystemManager()


__all__ = ["GlobalAndroidEcosystemManager", "get_manager"]
