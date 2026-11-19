"""Frontend-to-backend Infrastructure structure and contract checker."""
from pathlib import Path

class FrontendInfrastructureBackendInfrastructureConnector:
    def __init__(self):
        self.frontend_root = Path(__file__).resolve().parent
        self.repository_root = self.frontend_root.parents[1]
        self.backend_root = self.repository_root / "backend" / "infrastructure"
        self.backend_ecosystem = self.backend_root / "global_ecosystem" / "global_infrastructure_ecosystem"
        self.required_domains = (
            "backup", "billing", "cdn", "containers", "database", "dns", "domains",
            "email", "firewall", "ftp", "hosting", "ipam", "load_balancer", "model",
            "monitoring", "network", "object_storage", "security", "server", "ssl", "storage",
        )

    def connect(self):
        frontend_files = ("__init__.py", "manager.py", "manager.php",
                          "frontend_infrastructure_backend_infrastructure_connect.py",
                          "frontend_infrastructure_backend_infrastructure_connect.php")
        frontend_checks = {name: (self.frontend_root / name).is_file() for name in frontend_files}
        frontend_checks["global_ecosystem"] = (self.frontend_root / "global_ecosystem").is_dir()

        backend_checks = {
            "backend_infrastructure_root": self.backend_root.is_dir(),
            "backend_manager_py": (self.backend_root / "manager.py").is_file(),
            "backend_manager_php": (self.backend_root / "manager.php").is_file(),
            "backend_global_ecosystem_manager": (self.backend_root / "global_ecosystem" / "manager.py").is_file(),
            "backend_global_infrastructure_manager": (self.backend_ecosystem / "manager.py").is_file(),
        }
        domain_checks = {name: (self.backend_ecosystem / name).is_dir() for name in self.required_domains}
        backend_checks["all_21_domains_present"] = all(domain_checks.values())
        return {
            "name": "FRONTEND-BACKEND INFRASTRUCTURE CONNECTOR",
            "frontend": {"checks": frontend_checks, "healthy": all(frontend_checks.values())},
            "backend": {"checks": backend_checks, "domain_checks": domain_checks,
                        "expected_domain_count": len(self.required_domains),
                        "present_domain_count": sum(domain_checks.values()),
                        "healthy": all(backend_checks.values())},
            "connected": all(frontend_checks.values()) and all(backend_checks.values()),
            "connection_type": "local structure and contract validation; no provider mutations",
        }

def connect_infrastructure():
    return FrontendInfrastructureBackendInfrastructureConnector().connect()
