"""Frontend/backend infrastructure contract checker; no frontend domain files or folders."""
from pathlib import Path

from .manager import INFRASTRUCTURE_MODULES


class FrontendGlobalInfrastructureEcosystemConnector:
    def __init__(self):
        self.frontend_root = Path(__file__).resolve().parent
        self.repository_root = self.frontend_root.parents[3]
        self.backend_root = (
            self.repository_root
            / "backend"
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
        frontend_files = (
            "__init__.py",
            "manager.py",
            "manager.php",
            "frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.py",
            "frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.php",
        )
        frontend_checks = {
            name: (self.frontend_root / name).is_file()
            for name in frontend_files
        }
        backend_files = ("__init__.py", "manager.py", "manager.php")
        backend_checks = {
            name: (self.backend_root / name).is_file()
            for name in backend_files
        }
        backend_entry_checks = {
            "global_ecosystem_manager.py": (self.backend_entry / "manager.py").is_file(),
            "global_ecosystem_manager.php": (self.backend_entry / "manager.php").is_file(),
        }

        frontend_domain_names = set(INFRASTRUCTURE_MODULES)
        frontend_domain_files = [
            name for name in frontend_domain_names
            if (self.frontend_root / f"{name}.py").is_file()
        ]
        frontend_domain_folders = [
            name for name in frontend_domain_names
            if (self.frontend_root / name).is_dir()
        ]

        frontend_healthy = all(frontend_checks.values()) and not (
            frontend_domain_files or frontend_domain_folders
        )
        backend_healthy = (
            all(backend_domains.values())
            and all(backend_checks.values())
            and all(backend_entry_checks.values())
        )
        return {
            "name": "FRONTEND-BACKEND GLOBAL INFRASTRUCTURE CONNECTOR",
            "frontend": {
                "healthy": frontend_healthy,
                "file_checks": frontend_checks,
                "domain_file_count": len(frontend_domain_files),
                "domain_folder_count": len(frontend_domain_folders),
            },
            "backend": {
                "healthy": backend_healthy,
                "domain_checks": backend_domains,
                "file_checks": backend_checks,
                "entry_checks": backend_entry_checks,
                "expected_domain_count": len(INFRASTRUCTURE_MODULES),
                "present_domain_count": sum(backend_domains.values()),
            },
            "connected": frontend_healthy and backend_healthy,
            "connection_type": (
                "repository structure and contract validation; "
                "no external provider operations"
            ),
        }


def connect_infrastructure():
    return FrontendGlobalInfrastructureEcosystemConnector().connect()
