"""Validate the Backend Global Foundation to Frontend Global Infrastructure contract."""
from pathlib import Path


class BackendGlobalFoundationFrontendGlobalInfrastructureConnector:
    """Filesystem contract check; this is not a Python/PHP runtime bridge."""

    def __init__(self):
        self.foundation_root = Path(__file__).resolve().parent
        self.repository_root = self.foundation_root.parents[3]
        self.infrastructure_root = (
            self.repository_root
            / "frontend"
            / "infrastructure"
            / "global_ecosystem"
            / "global_infrastructure_ecosystem"
        )

    @staticmethod
    def _check(root):
        required = ("__init__.py", "manager.py", "manager.php")
        checks = {name: (root / name).is_file() for name in required}
        return {"path": str(root), "checks": checks, "healthy": all(checks.values())}

    def connect(self):
        foundation = self._check(self.foundation_root)
        infrastructure = self._check(self.infrastructure_root)
        return {
            "name": "BACKEND GLOBAL FOUNDATION - FRONTEND GLOBAL INFRASTRUCTURE CONNECTOR",
            "foundation": foundation,
            "infrastructure": infrastructure,
            "connected": foundation["healthy"] and infrastructure["healthy"],
            "connection_type": "filesystem contract check; not a runtime bridge",
        }


def connect_ecosystems():
    return BackendGlobalFoundationFrontendGlobalInfrastructureConnector().connect()
