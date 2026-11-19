"""Backend Infrastructure control-plane manager."""
from pathlib import Path

class BackendInfrastructureManager:
    NAME = "BACKEND INFRASTRUCTURE"
    VERSION = "1.0.0"

    def __init__(self):
        self.root = Path(__file__).resolve().parent

    def health(self):
        required = ("__init__.py", "controller.py", "repository.py", "service.py",
                    "hostinger_api.py", "hostinger_catalog.py", "global_ecosystem")
        checks = {name: (self.root / name).exists() for name in required}
        ecosystem = self.root / "global_ecosystem" / "global_infrastructure_ecosystem"
        checks["global_infrastructure_manager"] = (ecosystem / "manager.py").is_file()
        return {"name": self.NAME, "version": self.VERSION, "status": "READY" if all(checks.values()) else "INCOMPLETE",
                "checks": checks, "healthy": all(checks.values()),
                "provider_operations_enabled": False}

def get_manager():
    return BackendInfrastructureManager()
