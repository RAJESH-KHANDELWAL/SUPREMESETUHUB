"""Frontend Global Infrastructure Ecosystem contract manager."""
from pathlib import Path

class FrontendGlobalInfrastructureEcosystemManager:
    NAME = "FRONTEND GLOBAL INFRASTRUCTURE ECOSYSTEM"
    VERSION = "1.1.0"

    def __init__(self):
        self.root = Path(__file__).resolve().parent
        self.repository_root = self.root.parents[3]
        self.backend_root = self.repository_root / "backend" / "infrastructure" / "global_ecosystem" / "global_infrastructure_ecosystem"

    def health(self):
        expected = ("backup", "billing", "cdn", "containers", "database", "dns", "domains",
                    "email", "firewall", "ftp", "hosting", "ipam", "load_balancer", "model",
                    "monitoring", "network", "object_storage", "security", "server", "ssl", "storage")
        frontend_checks = {name: (self.root / name).exists() for name in ("__init__.py", "manager.py", "manager.php")}
        backend_checks = {name: (self.backend_root / name).is_dir() for name in expected}
        checks = {
            **{f"frontend_{name}": value for name, value in frontend_checks.items()},
            **{f"backend_{name}": value for name, value in backend_checks.items()},
            "backend_manager": (self.backend_root / "manager.py").is_file(),
        }
        present = sum(backend_checks.values())
        return {"name": self.NAME, "version": self.VERSION,
                "status": "READY" if all(checks.values()) else "INCOMPLETE",
                "checks": checks, "expected_domain_count": len(expected),
                "present_domain_count": present, "healthy": all(checks.values())}

def get_manager():
    return FrontendGlobalInfrastructureEcosystemManager()
