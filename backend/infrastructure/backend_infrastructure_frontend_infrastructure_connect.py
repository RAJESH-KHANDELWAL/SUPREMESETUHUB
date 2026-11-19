"""Backend-to-frontend Infrastructure structure and contract checker."""
from pathlib import Path


class BackendInfrastructureFrontendInfrastructureConnector:
    """Validate the paired frontend/backend infrastructure scaffolds.

    This checks local repository structure only. It does not call providers,
    change infrastructure, or claim that external services are operational.
    """

    REQUIRED_DOMAINS = (
        "backup", "billing", "cdn", "containers", "database", "dns", "domains",
        "email", "firewall", "ftp", "hosting", "ipam", "load_balancer", "model",
        "monitoring", "network", "object_storage", "security", "server", "ssl", "storage",
    )

    def __init__(self):
        self.backend_root = Path(__file__).resolve().parent
        self.repository_root = self.backend_root.parent.parent
        self.frontend_root = self.repository_root / "frontend" / "infrastructure"
        self.backend_ecosystem = (
            self.backend_root / "global_ecosystem" / "global_infrastructure_ecosystem"
        )
        self.frontend_ecosystem = (
            self.frontend_root / "global_ecosystem" / "global_infrastructure_ecosystem"
        )

    def connect(self):
        backend_files = (
            "__init__.py", "manager.py", "manager.php",
            "backend_infrastructure_frontend_infrastructure_connect.py",
            "backend_infrastructure_frontend_infrastructure_connect.php",
        )
        backend_checks = {
            name: (self.backend_root / name).is_file() for name in backend_files
        }
        backend_checks["global_ecosystem"] = (
            self.backend_root / "global_ecosystem"
        ).is_dir()

        frontend_files = ("__init__.py", "manager.py", "manager.php")
        frontend_checks = {
            name: (self.frontend_root / name).is_file() for name in frontend_files
        }
        frontend_checks["frontend_backend_connector_py"] = (
            self.frontend_root
            / "frontend_infrastructure_backend_infrastructure_connect.py"
        ).is_file()
        frontend_checks["frontend_backend_connector_php"] = (
            self.frontend_root
            / "frontend_infrastructure_backend_infrastructure_connect.php"
        ).is_file()
        frontend_checks["global_ecosystem"] = (
            self.frontend_root / "global_ecosystem"
        ).is_dir()

        backend_domain_checks = {
            name: (self.backend_ecosystem / name).is_dir()
            for name in self.REQUIRED_DOMAINS
        }
        frontend_checks["global_infrastructure_ecosystem_manager"] = (
            self.frontend_ecosystem / "manager.py"
        ).is_file()

        backend_healthy = all(backend_checks.values()) and all(
            backend_domain_checks.values()
        )
        frontend_healthy = all(frontend_checks.values())
        return {
            "name": "BACKEND-FRONTEND INFRASTRUCTURE CONNECTOR",
            "backend": {
                "checks": backend_checks,
                "domain_checks": backend_domain_checks,
                "expected_domain_count": len(self.REQUIRED_DOMAINS),
                "present_domain_count": sum(backend_domain_checks.values()),
                "healthy": backend_healthy,
            },
            "frontend": {
                "checks": frontend_checks,
                "healthy": frontend_healthy,
            },
            "connected": backend_healthy and frontend_healthy,
            "connection_type": (
                "local structure and contract validation; no provider mutations"
            ),
        }


def connect_infrastructure():
    return BackendInfrastructureFrontendInfrastructureConnector().connect()
