"""Backend Global Infrastructure -> Frontend Global Foundation contract checker."""
from pathlib import Path


class BackendGlobalInfrastructureFrontendGlobalFoundationConnector:
    """Check the global ecosystem scaffold; this is not a runtime bridge."""

    def __init__(self):
        self.infrastructure_root = Path(__file__).resolve().parent
        # infrastructure_root is four directory levels below the repository root.
        self.repository_root = self.infrastructure_root.parents[3]
        self.foundation_root = (
            self.repository_root / "frontend" / "foundation" / "global_ecosystem"
            / "global_foundation_ecosystem"
        )

    @staticmethod
    def _check(root: Path) -> dict:
        required = ("__init__.py", "manager.py", "manager.php")
        checks = {name: (root / name).is_file() for name in required}
        return {"path": str(root), "checks": checks, "healthy": all(checks.values())}

    def connect(self) -> dict:
        infrastructure = self._check(self.infrastructure_root)
        foundation = self._check(self.foundation_root)
        return {
            "name": "BACKEND GLOBAL INFRASTRUCTURE -> FRONTEND GLOBAL FOUNDATION",
            "infrastructure": infrastructure,
            "foundation": foundation,
            "connected": infrastructure["healthy"] and foundation["healthy"],
            "connection_type": "filesystem contract check; not a runtime bridge",
        }


def connect_ecosystems():
    return BackendGlobalInfrastructureFrontendGlobalFoundationConnector().connect()
