"""Connect and validate the frontend and backend Global Foundation Ecosystems."""
from pathlib import Path


class FrontendGlobalFoundationEcosystemBackendConnector:
    """Presence/contract check for both Global Foundation Ecosystem managers."""

    def __init__(self):
        self.frontend_root = Path(__file__).resolve().parent
        self.repository_root = self.frontend_root.parents[3]
        self.backend_root = (
            self.repository_root
            / "backend"
            / "foundation"
            / "global_ecosystem"
            / "global_foundation_ecosystem"
        )

    @staticmethod
    def _check(root):
        required = ("__init__.py", "manager.py", "manager.php")
        checks = {name: (root / name).is_file() for name in required}
        return {"path": str(root), "checks": checks, "healthy": all(checks.values())}

    def connect(self):
        frontend = self._check(self.frontend_root)
        backend = self._check(self.backend_root)
        return {
            "name": "FRONTEND-BACKEND GLOBAL FOUNDATION ECOSYSTEM CONNECTOR",
            "frontend": frontend,
            "backend": backend,
            "connected": frontend["healthy"] and backend["healthy"],
            "connection_type": "filesystem contract check; not a runtime bridge",
        }


def connect_foundations():
    return FrontendGlobalFoundationEcosystemBackendConnector().connect()
