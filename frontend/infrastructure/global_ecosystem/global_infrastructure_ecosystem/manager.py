"""Frontend Global Infrastructure Ecosystem manager; domain operations remain backend-owned."""
from pathlib import Path

INFRASTRUCTURE_MODULES = [
    "backup", "billing", "cdn", "containers", "database", "dns", "domains",
    "email", "firewall", "ftp", "hosting", "ipam", "load_balancer", "model",
    "monitoring", "network", "object_storage", "security", "server", "ssl", "storage",
]


class FrontendGlobalInfrastructureEcosystemManager:
    NAME = "FRONTEND GLOBAL INFRASTRUCTURE ECOSYSTEM"
    VERSION = "1.4.1"

    def __init__(self):
        self.root = Path(__file__).resolve().parent
        self.repository_root = self.root.parents[3]
        self.backend_root = (
            self.repository_root
            / "backend"
            / "infrastructure"
            / "global_ecosystem"
            / "global_infrastructure_ecosystem"
        )

    def health(self):
        backend = {name: (self.backend_root / name).is_dir() for name in INFRASTRUCTURE_MODULES}
        required = (
            "__init__.py",
            "manager.py",
            "manager.php",
            "frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.py",
            "frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.php",
        )
        files = {name: (self.root / name).is_file() for name in required}
        checks = {
            **{f"backend_domain_{name}": value for name, value in backend.items()},
            **{f"required_file_{name}": value for name, value in files.items()},
        }
        healthy = all(checks.values())
        return {
            "name": self.NAME,
            "version": self.VERSION,
            "status": "READY" if healthy else "INCOMPLETE",
            "expected_backend_domain_count": len(INFRASTRUCTURE_MODULES),
            "backend_present_domain_count": sum(backend.values()),
            "backend_domain_checks": backend,
            "required_file_checks": files,
            "frontend_domain_files_expected": 0,
            "frontend_domain_folders_expected": 0,
            "checks": checks,
            "healthy": healthy,
            "provider_operations_enabled": False,
        }


def get_manager():
    return FrontendGlobalInfrastructureEcosystemManager()
