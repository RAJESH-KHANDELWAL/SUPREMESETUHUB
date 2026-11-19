"""Backend/frontend global infrastructure ecosystem contract checker."""
from pathlib import Path

from .structure import INFRASTRUCTURE_MODULES


class BackendGlobalInfrastructureEcosystemConnector:
    """Validate canonical backend domains and the lean frontend scaffold."""

    def __init__(self):
        self.backend_root = Path(__file__).resolve().parent
        self.repository_root = self.backend_root.parents[3]
        self.frontend_root = (
            self.repository_root
            / "frontend"
            / "infrastructure"
            / "global_ecosystem"
            / "global_infrastructure_ecosystem"
        )
        self.backend_entry = self.repository_root / "backend" / "infrastructure" / "global_ecosystem"

    def connect(self):
        backend_domains = {
            name: (self.backend_root / name).is_dir()
            for name in INFRASTRUCTURE_MODULES
        }
        backend_files = {
            name: (self.backend_root / name).is_file()
            for name in (
                "__init__.py",
                "manager.py",
                "manager.php",
                "structure.py",
                "backend_global_infrastructure_ecosystem_frontend_global_infrastructure_ecosystem_connect.py",
                "backend_global_infrastructure_ecosystem_frontend_global_infrastructure_ecosystem_connect.php",
            )
        }
        frontend_files = {
            name: (self.frontend_root / name).is_file()
            for name in (
                "__init__.py",
                "manager.py",
                "manager.php",
                "frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.py",
                "frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.php",
            )
        }
        frontend_domain_files = [
            name for name in INFRASTRUCTURE_MODULES
            if (self.frontend_root / f"{name}.py").is_file()
        ]
        frontend_domain_folders = [
            name for name in INFRASTRUCTURE_MODULES
            if (self.frontend_root / name).is_dir()
        ]
        backend_entry_checks = {
            "global_ecosystem_manager.py": (self.backend_entry / "manager.py").is_file(),
            "global_ecosystem_manager.php": (self.backend_entry / "manager.php").is_file(),
        }

        backend_healthy = all(backend_domains.values()) and all(backend_files.values())
        frontend_healthy = (
            all(frontend_files.values())
            and not frontend_domain_files
            and not frontend_domain_folders
        )
        entry_healthy = all(backend_entry_checks.values())
        return {
            "name": "BACKEND-FRONTEND GLOBAL INFRASTRUCTURE CONNECTOR",
            "backend": {
                "healthy": backend_healthy,
                "domain_checks": backend_domains,
                "file_checks": backend_files,
                "expected_domain_count": len(INFRASTRUCTURE_MODULES),
                "present_domain_count": sum(backend_domains.values()),
            },
            "frontend": {
                "healthy": frontend_healthy,
                "file_checks": frontend_files,
                "domain_file_count": len(frontend_domain_files),
                "domain_folder_count": len(frontend_domain_folders),
            },
            "backend_entry": {"healthy": entry_healthy, "checks": backend_entry_checks},
            "connected": backend_healthy and frontend_healthy and entry_healthy,
            "connection_type": "repository structure and contract validation; not a runtime bridge",
        }


def connect_infrastructure():
    return BackendGlobalInfrastructureEcosystemConnector().connect()
