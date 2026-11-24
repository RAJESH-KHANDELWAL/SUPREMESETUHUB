"""Frontend Infrastructure -> Backend Foundation structural connector."""
from pathlib import Path


class FrontendInfrastructureBackendFoundationConnector:
    """Validate the root-level Frontend Infrastructure / Backend Foundation contract.

    This is a repository filesystem check, not a live service or runtime bridge.
    """

    def __init__(self):
        self.repository_root = Path(__file__).resolve().parents[2]
        self.frontend_infrastructure = self.repository_root / "frontend" / "infrastructure"
        self.backend_foundation = self.repository_root / "backend" / "foundation"

    @staticmethod
    def _checks(root: Path) -> dict:
        return {
            "root": root.is_dir(),
            "manager_py": (root / "manager.py").is_file(),
            "manager_php": (root / "manager.php").is_file(),
            "init_py": (root / "__init__.py").is_file(),
        }

    def connect(self) -> dict:
        frontend = self._checks(self.frontend_infrastructure)
        backend = self._checks(self.backend_foundation)
        connected = all(frontend.values()) and all(backend.values())
        return {
            "name": "FRONTEND INFRASTRUCTURE -> BACKEND FOUNDATION",
            "frontend_infrastructure": {"checks": frontend, "healthy": all(frontend.values())},
            "backend_foundation": {"checks": backend, "healthy": all(backend.values())},
            "connected": connected,
            "connection_type": "repository structure validation; no runtime bridge",
        }


def connect_foundation():
    return FrontendInfrastructureBackendFoundationConnector().connect()
