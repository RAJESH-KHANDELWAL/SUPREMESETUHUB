"""Backend Infrastructure control-plane manager."""
from pathlib import Path

class BackendInfrastructureManager:
    NAME = "BACKEND INFRASTRUCTURE"
    VERSION = "1.0.0"

    def __init__(self):
        self.root = Path(__file__).resolve().parent
        self.global_root = self.root / "global_ecosystem"

    def health(self):
        required = ("__init__.py", "controller.py", "repository.py", "service.py",
                    "hostinger_catalog.py", "global_ecosystem")
        checks = {name: (self.root / name).exists() for name in required}
        checks["global_hostinger_api"] = (self.global_root / "hostinger_api.py").is_file()
        checks["global_nsfwinfra"] = (self.global_root / "nsfwinfra.py").is_file()
        ecosystem = self.global_root / "global_infrastructure_ecosystem"
        checks["global_infrastructure_manager"] = (ecosystem / "manager.py").is_file()
        healthy = all(checks.values())
        return {"name": self.NAME, "version": self.VERSION, "status": "READY" if healthy else "INCOMPLETE",
                "checks": checks, "healthy": healthy,
                "provider_operations_enabled": False}

def get_manager():
    return BackendInfrastructureManager()
