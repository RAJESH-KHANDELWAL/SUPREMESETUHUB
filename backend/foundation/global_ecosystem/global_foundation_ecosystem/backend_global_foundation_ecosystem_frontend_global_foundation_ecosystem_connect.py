"""Connect and validate the backend and frontend Global Foundation Ecosystems."""
from pathlib import Path


class BackendGlobalFoundationEcosystemFrontendConnector:
    """Presence/contract check for both Global Foundation Ecosystem managers."""

    def __init__(self):
        self.backend_root = Path(__file__).resolve().parent
        self.repository_root = self.backend_root.parents[3]
        self.frontend_root = (
            self.repository_root
            / "frontend"
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
        backend = self._check(self.backend_root)
        frontend = self._check(self.frontend_root)
        return {
            "name": "BACKEND-FRONTEND GLOBAL FOUNDATION ECOSYSTEM CONNECTOR",
            "backend": backend,
            "frontend": frontend,
            "connected": backend["healthy"] and frontend["healthy"],
            "connection_type": "filesystem contract check; not a runtime bridge",
        }


def connect_foundations():
    return BackendGlobalFoundationEcosystemFrontendConnector().connect()
