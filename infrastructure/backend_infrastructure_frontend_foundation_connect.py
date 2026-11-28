"""Backend Infrastructure -> Frontend Foundation structural connector."""
from pathlib import Path


class BackendInfrastructureFrontendFoundationConnector:
    """Validate the root-level Backend Infrastructure / Frontend Foundation contract.

    This is a repository filesystem check, not a live service or runtime bridge.
    """

    def __init__(self):
        self.repository_root = Path(__file__).resolve().parents[2]
        self.backend_infrastructure = self.repository_root / "backend" / "infrastructure"
        self.frontend_foundation = self.repository_root / "frontend" / "foundation"

    @staticmethod
    def _checks(root: Path) -> dict:
        return {
            "root": root.is_dir(),
            "manager_py": (root / "manager.py").is_file(),
            "manager_php": (root / "manager.php").is_file(),
            "init_py": (root / "__init__.py").is_file(),
        }

    def connect(self) -> dict:
        backend = self._checks(self.backend_infrastructure)
        frontend = self._checks(self.frontend_foundation)
        connected = all(backend.values()) and all(frontend.values())
        return {
            "name": "BACKEND INFRASTRUCTURE -> FRONTEND FOUNDATION",
            "backend_infrastructure": {"checks": backend, "healthy": all(backend.values())},
            "frontend_foundation": {"checks": frontend, "healthy": all(frontend.values())},
            "connected": connected,
            "connection_type": "repository structure validation; no runtime bridge",
        }


def connect_foundation():
    return BackendInfrastructureFrontendFoundationConnector().connect()
